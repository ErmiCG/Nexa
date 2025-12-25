from backend.db import get_db

def set_budget(user_id, month, amount):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM budgets WHERE user_id=%s", (user_id,))
    existing = cursor.fetchone()

    if existing:
        cursor.execute(
            "UPDATE budgets SET month=%s, amount=%s WHERE user_id=%s",
            (month, amount, user_id)
        )
    else:
        cursor.execute(
            "INSERT INTO budgets (user_id, month, amount) VALUES (%s,%s,%s)",
            (user_id, month, amount)
        )

    conn.commit()
    cursor.close()
    conn.close()


def get_budget_status(user_id):
    conn = get_db()
    cursor = conn.cursor()

    # Fetch the user's budget
    cursor.execute("SELECT amount FROM budgets WHERE user_id=%s", (user_id,))
    row = cursor.fetchone()
    total_budget = row[0] if row else 0

    # Fetch sum of expenses
    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id=%s AND type='Expense'",
        (user_id,)
    )
    spent = cursor.fetchone()[0] or 0

    # Calculate remaining
    remaining = total_budget - spent

    # Progress capped at 100%
    progress = 0
    if total_budget > 0:
        progress = round((spent / total_budget) * 100, 1)
        if progress > 100:
            progress = 100

    cursor.close()
    conn.close()

    return {
        'total_budget': total_budget,
        'spent': spent,
        'remaining': remaining,
        'progress': progress
    }

