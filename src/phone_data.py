"""Reusable validation and descriptive analysis for phone specifications."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

EXPECTED_COLUMNS = [
    "PID", "Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem", "Px_h", "Px_w",
    "Scr_h", "Scr_w", "PC", "FC", "Int_Mem", "Bty_Pwr", "RAM",
    "Depth", "Weight", "Price",
]
BINARY_COLUMNS = ["Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem"]
NUMERIC_COLUMNS = [column for column in EXPECTED_COLUMNS if column not in {"PID", *BINARY_COLUMNS}]
SPECIFICATION_COLUMNS = [column for column in NUMERIC_COLUMNS if column != "Price"]


def validate_phone_data(frame: pd.DataFrame) -> pd.DataFrame:
    """Validate schema and values without mutating the supplied DataFrame."""
    if not isinstance(frame, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")
    if frame.empty:
        raise ValueError("Phone dataset is empty.")
    if frame.columns.tolist() != EXPECTED_COLUMNS:
        raise ValueError(f"Expected columns in this order: {EXPECTED_COLUMNS}")
    if frame.isna().any().any():
        raise ValueError("Phone dataset contains missing values.")
    if frame["PID"].astype(str).str.strip().eq("").any():
        raise ValueError("Product IDs must not be blank.")
    normalized_ids = frame["PID"].astype(str).str.strip()
    if normalized_ids.duplicated().any():
        raise ValueError("Product IDs must be unique after trimming whitespace.")

    for column in BINARY_COLUMNS:
        values = set(frame[column].astype(str).str.strip().str.lower())
        if not values <= {"yes", "no"}:
            raise ValueError(f"{column} must contain only yes/no values.")

    numeric = frame[NUMERIC_COLUMNS].apply(pd.to_numeric, errors="coerce")
    if numeric.isna().any().any():
        raise ValueError("Numeric specifications contain non-numeric values.")
    values = numeric.to_numpy(dtype=float)
    if not np.isfinite(values).all():
        raise ValueError("Numeric specifications contain non-finite values.")
    if (numeric < 0).any().any():
        raise ValueError("Numeric specifications must not be negative.")
    if numeric["Price"].nunique(dropna=False) < 2:
        raise ValueError("Price must vary for comparative price analysis.")
    return frame


def load_phone_data(path: str | Path) -> pd.DataFrame:
    """Load a CSV file and apply the project schema and value checks."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Phone dataset not found: {path}")
    frame = pd.read_csv(path)
    validate_phone_data(frame)
    return frame


def summarize_phone_data(frame: pd.DataFrame) -> pd.DataFrame:
    """Return distribution statistics for numeric specification fields."""
    validate_phone_data(frame)
    numeric = frame[NUMERIC_COLUMNS].apply(pd.to_numeric, errors="raise")
    summary = numeric.agg(["count", "mean", "median", "std", "min", "max"]).T
    summary["q1"] = numeric.quantile(0.25)
    summary["q3"] = numeric.quantile(0.75)
    summary["iqr"] = summary["q3"] - summary["q1"]
    summary.index.name = "feature"
    return summary[["count", "mean", "median", "std", "min", "q1", "q3", "max", "iqr"]].round(2)


def price_rank_correlations(frame: pd.DataFrame) -> pd.Series:
    """Rank numeric specifications by Spearman association with listed price."""
    validate_phone_data(frame)
    numeric = frame[NUMERIC_COLUMNS].apply(pd.to_numeric, errors="raise")
    predictors = numeric[SPECIFICATION_COLUMNS]
    variable_predictors = predictors.columns[predictors.nunique(dropna=False) > 1]
    if len(variable_predictors) == 0:
        return pd.Series(dtype=float, name="spearman_rho_with_listed_price")
    correlations = predictors[variable_predictors].corrwith(
        numeric["Price"], method="spearman"
    )
    return correlations.sort_values(key=lambda values: values.abs(), ascending=False).rename(
        "spearman_rho_with_listed_price"
    ).round(3)


def price_band_summary(frame: pd.DataFrame, bands: int = 3) -> pd.DataFrame:
    """Summarize product specifications across quantile-based listed-price bands.

    Bands are relative to this supplied sample, not market-defined price tiers.
    Duplicate quantile boundaries are dropped for datasets with tied prices.
    """
    validate_phone_data(frame)
    if not isinstance(bands, int) or bands < 2:
        raise ValueError("bands must be an integer of at least 2.")
    working = frame.copy()
    working["Price"] = pd.to_numeric(working["Price"], errors="raise")
    labels = [f"Sample price band {i + 1}" for i in range(bands)]
    working["price_band"] = pd.qcut(
        working["Price"], q=bands, labels=False, duplicates="drop"
    )
    actual_bands = int(working["price_band"].nunique())
    working["price_band"] = working["price_band"].map(
        {i: labels[i] for i in range(actual_bands)}
    )
    result = working.groupby("price_band", observed=True).agg(
        product_count=("PID", "count"),
        mean_listed_price=("Price", "mean"),
        median_listed_price=("Price", "median"),
        mean_ram=("RAM", "mean"),
        mean_internal_memory=("Int_Mem", "mean"),
        mean_battery_power=("Bty_Pwr", "mean"),
        mean_weight=("Weight", "mean"),
    )
    return result.round(2)
