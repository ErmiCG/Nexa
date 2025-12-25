from backend.db import get_db

def create_goal(user_id, name, target_amount):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO goals (user_id, name, target_amount) VALUES (%s,%s,%s)",
        (user_id, name, target_amount)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_goals(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, target_amount, current_amount FROM goals WHERE user_id=%s",
        (user_id,)
    )
    goals = cursor.fetchall()
    cursor.close()
    conn.close()
    return goals
def add_savings(goal_id, amount):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE goals SET current_amount = current_amount + %s WHERE id=%s",
        (amount, goal_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
