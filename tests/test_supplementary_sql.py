import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "smartphones_india_cleaned.csv"
SQL_FILE = ROOT / "sql" / "smartphone_market_analysis.sql"


def _select_statements(sql_text):
    without_comments = "\n".join(
        line for line in sql_text.splitlines()
        if not line.lstrip().startswith("--")
    )
    return [
        statement.strip()
        for statement in without_comments.split(";")
        if statement.strip()
    ]


def test_all_supplementary_market_sql_queries_execute_in_sqlite():
    frame = pd.read_csv(DATA)
    with sqlite3.connect(":memory:") as connection:
        frame.to_sql("smartphones", connection, index=False, if_exists="replace")
        statements = _select_statements(SQL_FILE.read_text(encoding="utf-8"))
        assert len(statements) == 5
        results = [pd.read_sql_query(statement, connection) for statement in statements]

    assert results[0].loc[0, "phone_models"] == 758
    assert results[0].loc[0, "brands"] > 0
    assert results[1]["brand"].notna().all()
    assert results[2]["models"].gt(0).all()
    assert results[3]["models"].sum() == 758
    assert results[4]["models"].sum() == 758
