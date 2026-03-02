# models/budget.py

from typing import Dict
import pandas as pd


class BudgetManager:
    def __init__(self, df: pd.DataFrame, category_limits: Dict[str, float]):
        self.df = df.copy()
        self.category_limits = category_limits

    def budget_summary(self) -> pd.DataFrame:
        actuals = (
            self.df.groupby("category", as_index=False)["amount"]
            .sum()
            .rename(columns={"amount": "actual"})
        )

        budgets = pd.DataFrame(
            list(self.category_limits.items()),
            columns=["category", "budget"]
        )

        summary = actuals.merge(budgets, on="category", how="left")
        summary["budget"] = summary["budget"].fillna(0.0)
        summary["difference"] = summary["budget"] - summary["actual"]
        summary["status"] = summary["difference"].apply(
            lambda x: "OVERSPENT" if x < 0 else "WITHIN BUDGET"
        )

        return summary.sort_values(by="actual", ascending=False)