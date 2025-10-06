# load.py
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Загружает CSV и возвращает DataFrame."""
    return pd.read_csv(path)