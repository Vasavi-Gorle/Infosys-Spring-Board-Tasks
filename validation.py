# validation.py
def validate_fitness_df(df):
    issues=[]
    required = ['timestamp','device_id','heart_rate','steps']
    missing = [c for c in required if c not in df.columns]
    if missing:
        issues.append(f"Missing columns: {missing}")
    if 'timestamp' in df.columns:
        pct = df['timestamp'].notna().mean()
        if pct < 0.9:
            issues.append(f"Low timestamp parse rate: {pct:.1%}")
    for c in ['heart_rate','steps']:
        if c in df.columns:
            n_non_num = df[c].apply(lambda x: pd.isna(x) or pd.api.types.is_number(x)).eq(False).sum()
            if n_non_num > 0:
                issues.append(f"{n_non_num} non-numeric values in {c}")
    return issues
