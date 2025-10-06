# demo_compare.py
import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from loader import load_fitness_data

def measure_load(path, repeats=3):
    times=[]
    last_df=None
    for _ in range(repeats):
        t0=time.perf_counter()
        try:
            df = load_fitness_data(path, file_type='auto')
            ok=True; err=None
        except Exception as e:
            df=None; ok=False; err=str(e)
        t1=time.perf_counter()
        times.append(t1-t0)
        last_df = df
        if not ok:
            break
    return {
        "path": str(path),
        "format": Path(path).suffix.lstrip('.'),
        "size_kb": round(os.path.getsize(path)/1024, 2),
        "load_time_s": round(min(times) if times else None, 4),
        "success": last_df is not None,
        "error": err,
        "rows": len(last_df) if last_df is not None else None
    }

def compare(paths):
    rows=[]
    for p in paths:
        rows.append(measure_load(p))
    df=pd.DataFrame(rows)
    return df

# Example usage:
# files = ["data/fitness_sample.csv","data/fitness_sample_nested.json","data/fitness_sample.xlsx"]
# summary = compare(files)
# Plot successful ones:
# s = summary[summary.success]
# plt.bar(s['format'], s['load_time_s'])
# plt.ylabel('load time (s)'); plt.title('Load time by format'); plt.savefig('format_load_time.png')
