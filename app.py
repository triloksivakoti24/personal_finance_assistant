# app.py

from utils.helpers import load_data
from models.expense import ExpenseAnalyzer
from models.budget import BudgetManager


def main():
    print("Application started")

    df = load_data()

    expense_analyzer = ExpenseAnalyzer(df)
    total_expense = expense_analyzer.total_expense()
    expense_by_category = expense_analyzer.expense_by_category()

    # Budgets aligned with actual dataset categories
    category_budgets = {
        "Restaurant": 3000,
        "Market": 4000,
        "Coffee": 1500,
        "Transport": 2000,
        "Phone": 1000,
        "Other": 1000,
        "Communal": 2000,
        "Events": 1500,
    }

    budget_manager = BudgetManager(df, category_budgets)
    budget_report = budget_manager.budget_summary()

    print("\nTOTAL EXPENSE:")
    print(total_expense)

    print("\nEXPENSE BY CATEGORY:")
    print(expense_by_category.to_string(index=False))

    print("\nBUDGET REPORT:")
    print(budget_report.to_string(index=False))


if __name__ == "__main__":
    main()