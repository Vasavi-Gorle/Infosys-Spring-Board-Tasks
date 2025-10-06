# loader.py
import json
from pathlib import Path
import pandas as pd
import xml.etree.ElementTree as ET

def load_fitness_data(file_path, file_type='auto'):
    """
    Load fitness data from csv / nested json / excel.
    Returns a pandas.DataFrame (raises informative exceptions on error).
    """
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    ft = (file_type.lower() if file_type != 'auto' else p.suffix.lower().lstrip('.'))
    try:
        if ft in ('csv','txt'):
            # Try default fast read, fallback to tolerant read if errors
            try:
                df = pd.read_csv(p)
            except Exception:
                # tolerant fallback (skip bad lines)
                df = pd.read_csv(p, engine='python', on_bad_lines='skip')
        elif ft == 'json':
            # open and detect nested structure like: [ {device_id, date, readings: [ ... ]}, ... ]
            with open(p, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list) and data and isinstance(data[0], dict) and 'readings' in data[0]:
                # Flatten sessions -> readings
                rows = []
                for session in data:
                    device = session.get('device_id')
                    date = session.get('date')
                    for r in session.get('readings', []):
                        if 'device_id' not in r and device is not None:
                            r['device_id'] = device
                        if 'timestamp' not in r and date is not None:
                            r['timestamp'] = date
                        rows.append(r)
                df = pd.DataFrame.from_records(rows)
            else:
                # try normal json read; support both records and ndjson
                try:
                    df = pd.read_json(p, orient='records')
                except ValueError:
                    df = pd.read_json(p, lines=True)
        elif ft in ('xls','xlsx'):
            df = pd.read_excel(p)
        else:
            raise ValueError(f"Unsupported or unknown format: {ft}")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error: {e} — file likely malformed or truncated. Try opening in a text editor.")
    except Exception as e:
        raise RuntimeError(f"Failed to load '{file_path}'. Error: {e}. Hint: check encoding/truncation or open file to inspect.")

    # Standardize and coerce types
    df.columns = [str(c).strip() for c in df.columns]
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    for c in ['heart_rate', 'steps', 'calories']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    return df
