"""tests for the data module."""

import pandas as pd
import pytest

from ml_foundations.data import drop_missing

def test_drop_missing_removes_high_missing_columns() -> None:
    df = pd.DataFrame(
        {
            "keep": [1,2,3,4],
            "mostly_missing": [1, None, None, None],
        }
    )
    result = drop_missing(df,threshold=0.5)
    assert "keep" in result.columns
    assert "mostly_missing" not in result.columns

def test_drop_missing_keeps_columns_under_threshold() -> None:
    df = pd.DataFrame({"a": [1, None, 3, 4], "b": [1,2,3,4]})
    result = drop_missing(df,threshold=0.5)
    assert list(result.columns) == ["a","b"]