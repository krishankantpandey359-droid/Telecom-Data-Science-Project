from pathlib import Path

import pandas as pd
import pytest

from src.phone_data import (
    EXPECTED_COLUMNS,
    load_phone_data,
    price_rank_correlations,
    summarize_phone_data,
    validate_phone_data,
)

DATA_PATH = Path(__file__).resolve().parents[1] / "Telecom Dataset.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def test_csv_loads_with_expected_schema_and_shape():
    frame = load_phone_data(DATA_PATH)
    assert frame.shape == (50, 17)
    assert frame.columns.tolist() == EXPECTED_COLUMNS


def test_product_ids_are_unique_and_present():
    frame = load_data()
    assert frame["PID"].notna().all()
    assert frame["PID"].is_unique


def test_binary_features_are_yes_no():
    frame = load_data()
    for column in ["Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem"]:
        assert set(frame[column].str.lower()) <= {"yes", "no"}


def test_numeric_fields_are_finite_and_non_negative():
    frame = load_data()
    numeric = frame.drop(columns=["PID", "Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem"])
    assert numeric.notna().all().all()
    assert (numeric >= 0).all().all()


def test_summary_covers_all_numeric_fields():
    summary = summarize_phone_data(load_data())
    assert summary.index.tolist() == [
        "Px_h", "Px_w", "Scr_h", "Scr_w", "PC", "FC", "Int_Mem",
        "Bty_Pwr", "RAM", "Depth", "Weight", "Price",
    ]
    assert summary["count"].eq(50).all()
    assert (summary["q1"] <= summary["q3"]).all()


def test_price_correlations_are_bounded_and_ranked():
    correlations = price_rank_correlations(load_data())
    assert "Price" not in correlations.index
    assert correlations.between(-1, 1).all()
    assert correlations.abs().is_monotonic_decreasing


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("PID", "", "must not be blank"),
        ("PID", "duplicate", "must be unique"),
        ("Blue", "unknown", "yes/no"),
        ("Price", "unknown", "non-numeric"),
        ("Price", float("inf"), "non-finite"),
        ("RAM", -1, "must not be negative"),
    ],
)
def test_validation_rejects_invalid_values(column, value, message):
    frame = load_data()
    frame[column] = frame[column].astype(object)
    frame.loc[0, column] = value
    if column == "PID" and value == "duplicate":
        frame.loc[1, column] = "duplicate"
    with pytest.raises(ValueError, match=message):
        validate_phone_data(frame)


def test_validation_rejects_missing_values():
    frame = load_data()
    frame.loc[0, "Price"] = None
    with pytest.raises(ValueError, match="missing values"):
        validate_phone_data(frame)


def test_validation_rejects_wrong_column_order():
    frame = load_data()[list(reversed(EXPECTED_COLUMNS))]
    with pytest.raises(ValueError, match="columns in this order"):
        validate_phone_data(frame)


def test_analysis_does_not_mutate_input():
    frame = load_data()
    original = frame.copy(deep=True)
    summarize_phone_data(frame)
    price_rank_correlations(frame)
    pd.testing.assert_frame_equal(frame, original)


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_phone_data(tmp_path / "missing.csv")
