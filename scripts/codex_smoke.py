"""Run bounded native Codex smoke checks through an existing ChatGPT login."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
INSTALLED=Path.home()/'.codex/plugins/cache/cognition-os-local/cognition-os/0.1.0'
PROMPTS={
    'numerical':f'''Use the installed cognition-os plugin's quantitative-decision skill for this native integration smoke test. The installed plugin root is {INSTALLED}. Load its SKILL.md and referenced calculation guidance from that installed copy; do not read the source checkout. Compute gross and net expected value with probability 0.65, upside 2.4, downside 0.3, costs 0.8, all in USD million. Execute the packaged calculation helper if permitted and report the observed result, units, method, and limitations. Do not infer a real-world approval or calibrated confidence. No network, other plugins, delegation, file changes, installations or credential access. Use at most eight tool calls and give a concise final answer identifying the skill/resources actually loaded and whether the helper ran. If permissions prevent a step, report it rather than pretending it ran.''',
    'incident':f'''Use the installed cognition-os plugin's root-cause-analysis skill for this native integration smoke test. The installed plugin root is {INSTALLED}. Load that SKILL.md and only relevant shared resources from that installed copy; do not read the source checkout. User case: MariaDB service fails repeatedly at night. No logs, timestamps, process/resource measurements, unaffected comparison systems or change history have been provided. Use Kepner-Tregoe to assess what can be concluded and provide safe next diagnostic checks. Do not inspect this computer's real services or files, run recovery commands, invent evidence, or label a root cause verified. No network, other plugins, delegation, file changes, installations or credential access. Use at most eight tool calls and give a concise answer with IS/IS NOT gaps, candidate hypotheses, falsifying tests and a conditional verdict. Identify which installed skill and framework resource you actually loaded.'''
}

def run(case):
    codex=shutil.which('codex.cmd') or shutil.which('codex.exe')
    if not codex:raise RuntimeError('Codex executable unavailable')
    login=subprocess.run([codex,'login','status'],capture_output=True,text=True,timeout=20)
    if 'Logged in using ChatGPT' not in login.stdout+login.stderr:
        raise RuntimeError('ChatGPT authentication not confirmed; refusing API-billed fallback')
    if not (INSTALLED/'plugin.json').is_file():raise RuntimeError('Expected installed plugin unavailable')
    workspace=ROOT/'tmp/native-smoke'/case;workspace.mkdir(parents=True,exist_ok=True)
    output=ROOT/f'docs/evidence/codex-smoke-{case}.txt'
    events=ROOT/f'docs/evidence/codex-smoke-{case}.jsonl'
    command=[codex,'exec','--ephemeral','--skip-git-repo-check','--sandbox','read-only','--json','-C',str(workspace),'-o',str(output),'-']
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
    start=time.monotonic()
    with events.open('w',encoding='utf-8') as log:
        process=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=log,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace',env=env)
        try:
            _,stderr=process.communicate(PROMPTS[case],timeout=180)
            status='COMPLETED' if process.returncode==0 else 'FAILED'
        except subprocess.TimeoutExpired:
            process.kill();_,stderr=process.communicate();status='TIMEOUT'
    record={'case':case,'authentication':'ChatGPT login verified; no API fallback','command':command,'prompt':PROMPTS[case],
        'status':status,'returncode':process.returncode,'elapsed_seconds':time.monotonic()-start,'stderr':stderr,
        'response':output.read_text(encoding='utf-8') if output.exists() else None,'evaluation':'REQUIRES_REVIEW; process success alone is not behavioral acceptance'}
    (ROOT/f'docs/evidence/codex-smoke-{case}.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    print(json.dumps(record,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('case',choices=PROMPTS);run(parser.parse_args().case)
