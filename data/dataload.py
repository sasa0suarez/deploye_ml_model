import pandas as pd
from pathlib import Path

def data_import(path_import: str) -> pd.DataFrame:
    """Loads a CSV dataset from a given path and returns a DataFrame."""
    df = pd.read_csv(path_import)
    return df

def data_export(df: pd.DataFrame, path_export: str) -> None:
    """Exports a DataFrame to a CSV file at the specified path."""
    # Ensure the parent directory exists before saving
    Path(path_export).parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(path_export, index=False)