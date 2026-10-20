"""Read-only advisory checks for explicitly edited .cognition/artifacts JSON files."""
import hashlib
import json
import re
import stat
from pathlib import Path
from . import augmentation as a

MAX_BYTES = 1048576
MAX_FILES = 8


def linked(path):
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & 0x400)


def handle_event(event):
    if not isinstance(event, dict) or event.get('hook_event_name') != 'PostToolUse':
        return {}
    tool = event.get('tool_name')
    if tool not in ['Write', 'Edit', 'apply_patch']:
        return {}
    cwd = event.get('cwd')
    if not isinstance(cwd, str) or not Path(cwd).is_absolute():
        return {}
    root = Path(cwd).resolve(strict=True)
    args = event.get('tool_input', {})
    if not isinstance(args, dict):
        return {}
    candidates = []
    if tool in ['Write', 'Edit'] and isinstance(args.get('file_path'), str):
        candidates.append(args['file_path'])
    if tool == 'apply_patch' and isinstance(args.get('command'), str):
        candidates += re.findall(r'^\*\*\* (?:Add File|Update File|Move to): (.+)$', args['command'], re.M)
    issues = 0; inspected = set(); hashes = set(); mentioned = set()
    for name in candidates:
        relative = None
        try:
            target = Path(name)
            target = target if target.is_absolute() else root/target
            relative = target.relative_to(root)
            if '..' in relative.parts or relative.parts[:2] != ('.cognition', 'artifacts') or target.suffix != '.json':
                continue
            if target in mentioned:
                continue
            mentioned.add(target)
            if len(mentioned) > MAX_FILES:
                issues += 1
                break
            current = root
            for part in relative.parts:
                current = current/part
                if linked(current):
                    raise ValueError('Linked artifact excluded')
            resolved = target.resolve(strict=True)
            resolved.relative_to(root/'.cognition/artifacts')
            if resolved in inspected or not stat.S_ISREG(resolved.stat().st_mode):
                continue
            inspected.add(resolved)
            with resolved.open('rb') as stream:
                raw = stream.read(MAX_BYTES+1)
            if len(raw) > MAX_BYTES:
                issues += 1; continue
            digest = hashlib.sha256(raw).hexdigest()
            if digest in hashes:
                continue
            hashes.add(digest)
            data = json.loads(raw.decode('utf-8-sig'), parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON')))
            a.check(data, a.RESULT)
        except (OSError, ValueError, UnicodeError, TypeError, RecursionError):
            # Do not echo artifact content, field names or attacker-controlled paths into host instructions.
            if relative is not None and relative.parts[:2] == ('.cognition', 'artifacts') and target.exists() and not target.is_symlink():
                issues += 1
    if not issues:
        return {}
    return {'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext':
            f'Cognition OS advisory artifact check: {issues} artifact(s) could not be validated. '
            'Inspect the edited .cognition/artifacts JSON against schemas/advisory-result.schema.json. '
            'This is structural advisory feedback; it does not undo edits or certify correctness.'}}
