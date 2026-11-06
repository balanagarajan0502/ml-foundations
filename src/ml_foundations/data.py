"""Data loading and cleaning utilities for ML workflows."""
from pathlib import Path
import pandas as pd
def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame

    Args:
        path: Path to the Csv file.
    Returns:
        The loaded DataFrame.
    Raises:
        FileNotFoundEroor: If the path does not exist.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No file found at {path}")
    return pd.read_csv(path)
def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns with more than 'threshold' fraction of missing values.
    Args:
        df: Input DataFrame.
        threshold: Fraction of allowed missing values (0 to 1).
        
    returns:
        dataFrame with high-missing columns removed.
    """
    missing_fraction = df.isna().mean()
    keep = missing_fraction[missing_fraction <= threshold].index
    return df[keep].copy()
    