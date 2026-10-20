"""Bounded stdin hook adapter. Always advisory; no model, network, writes or blocking."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cognition.artifact_validation import handle_event


def main():
    try:
        raw = sys.stdin.buffer.read(262145)
        if len(raw) > 262144:
            raise ValueError('Hook payload exceeds bound')
        payload = json.loads(raw, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite payload')))
        print(json.dumps(handle_event(payload), ensure_ascii=True))
    except (ValueError, TypeError, OSError, RecursionError):
        print(json.dumps({'systemMessage': 'Cognition OS advisory hook unavailable: input or artifact could not be inspected. No validation success is claimed.'}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
