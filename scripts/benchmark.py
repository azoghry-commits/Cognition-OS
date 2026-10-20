"""Only local deterministic timing; never presents this as native model performance."""
import json
import platform
import statistics
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from cognition.mathematics import simulate

def run():
    inputs=json.loads((ROOT/'references/examples/simulation.json').read_text())['inputs']
    times=[]
    for _ in range(7):
        start=time.perf_counter();result=simulate(**inputs);times.append((time.perf_counter()-start)*1000)
    output={'scope':'Local Python helper only, not host latency/token/quality','python':platform.python_version(),'platform':platform.platform(),'runs':7,'inputs':inputs,'milliseconds':times,'median_ms':statistics.median(times),'result':result,'native_baseline_comparison':'NOT_VERIFIED'}
    (ROOT/'docs/evidence/benchmark.json').write_text(json.dumps(output,indent=2),encoding='utf-8');print(json.dumps(output,indent=2))
if __name__=='__main__':run()
