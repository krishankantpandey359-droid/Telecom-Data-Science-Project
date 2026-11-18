import ast
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "Telecom_Data_Science_Project_COMPLETE (1).ipynb"


def _embedded_dataframe():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    source = "".join(notebook["cells"][4]["source"])
    tree = ast.parse(source)
    assignment = next(
        node for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "csv_data" for target in node.targets)
    )
    csv_text = ast.literal_eval(assignment.value)
    from io import StringIO
    return pd.read_csv(StringIO(csv_text))


def test_embedded_mobile_dataset_has_expected_shape_and_schema():
    frame = _embedded_dataframe()
    expected = {
        "PID", "Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem", "Px_h", "Px_w",
        "Scr_h", "Scr_w", "PC", "FC", "Int_Mem", "Bty_Pwr", "RAM",
        "Depth", "Weight", "Price",
    }
    assert frame.shape == (50, 17)
    assert set(frame.columns) == expected


def test_product_identifiers_are_unique_and_complete():
    frame = _embedded_dataframe()
    assert frame["PID"].notna().all()
    assert frame["PID"].is_unique


def test_numeric_fields_are_finite_and_non_negative():
    frame = _embedded_dataframe()
    columns = ["Px_h", "Px_w", "Scr_h", "Scr_w", "PC", "FC", "Int_Mem",
               "Bty_Pwr", "RAM", "Depth", "Weight", "Price"]
    numeric = frame[columns].apply(pd.to_numeric, errors="coerce")
    assert numeric.notna().all().all()
    assert numeric.ge(0).all().all()


def test_boolean_specifications_use_yes_no_only():
    frame = _embedded_dataframe()
    for column in ["Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem"]:
        values = set(frame[column].dropna().astype(str).str.strip().str.lower())
        assert values <= {"yes", "no"}
        assert frame[column].notna().all()


def test_analysis_notebook_excludes_pid_from_categorical_plots():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    sources = [ "".join(cell.get("source", [])) for cell in notebook["cells"] ]
    assert any('if c != "pid"' in source for source in sources)
