# converter.py
from pathlib import Path
from loader import load_fitness_data

def convert_file(in_path, out_path):
    df = load_fitness_data(in_path)
    out_ext = Path(out_path).suffix.lstrip('.')
    if out_ext in ('csv','txt'):
        df.to_csv(out_path, index=False)
    elif out_ext in ('xlsx','xls'):
        df.to_excel(out_path, index=False)
    elif out_ext == 'json':
        df.to_json(out_path, orient='records', date_format='iso')
    elif out_ext == 'parquet':
        df.to_parquet(out_path, index=False)
    else:
        raise ValueError("Unsupported output format.")
    return out_path
