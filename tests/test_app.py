# tests/test_app.py

import pandas as pd
from utils.helpers import load_data
from models.expense import ExpenseAnalyzer
from models.budget import BudgetManager


def test_data_loading():
    df = load_data()
    assert not df.empty
    assert {"date", "category", "amount"}.issubset(df.columns)


def test_total_expense():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "category": ["Food", "Food"],
        "amount": [100, 200],
    })
    analyzer = ExpenseAnalyzer(df)
    assert analyzer.total_expense() == 300.0


def test_budget_status():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2024-01-01"]),
        "category": ["Transport"],
        "amount": [1500],
    })
    manager = BudgetManager(df, {"Transport": 1000})
    summary = manager.budget_summary()
    assert summary.iloc[0]["status"] == "OVERSPENT"