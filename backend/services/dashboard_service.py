from backend.db import get_db
from datetime import date

def get_dashboard_data(user_id):
    conn = get_db()
    cursor = conn.cursor()

    today = date.today()

    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id=%s AND date=%s AND type='Expense'",
        (user_id, today)
    )
    today_expense = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id=%s AND type='Income'",
        (user_id,)
    )
    monthly_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT amount FROM budgets WHERE user_id=%s", (user_id,))
    row = cursor.fetchone()
    budget_amount = row[0] if row else 0

    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id=%s AND type='Expense'",
        (user_id,)
    )
    spent = cursor.fetchone()[0] or 0

    budget_used = min(100, int((spent / budget_amount) * 100)) if budget_amount else 0

    saving_progress = monthly_income - spent

    cursor.close()
    conn.close()

    return {
        'today_expense': today_expense,
        'monthly_income': monthly_income,
        'budget_used': budget_used,
        'saving_progress': saving_progress
    }
