# models/expense.py

import pandas as pd


class ExpenseAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def total_expense(self) -> float:
        return float(self.df["amount"].sum())

    def expense_by_category(self) -> pd.DataFrame:
        return (
            self.df.groupby("category", as_index=False)["amount"]
            .sum()
            .sort_values(by="amount", ascending=False)
        )

    def daily_expense(self) -> pd.DataFrame:
        self.df["date_only"] = self.df["date"].dt.date
        return (
            self.df.groupby("date_only", as_index=False)["amount"]
            .sum()
            .sort_values(by="date_only")
        )