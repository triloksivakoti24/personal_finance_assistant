# utils/helpers.py

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "data.csv"


def load_data() -> pd.DataFrame:
    """
    Load and validate expense dataset.
    """
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    required_cols = {"date", "category", "amount"}
    if not required_cols.issubset(df.columns):
        raise ValueError("CSV must contain date, category, amount columns")

    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["category"] = df["category"].str.strip()
    df["amount"] = pd.to_numeric(df["amount"], errors="raise")

    return df