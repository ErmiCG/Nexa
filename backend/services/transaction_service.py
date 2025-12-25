# transaction_service.py
from backend.db import get_db

def add_transaction(user_id, amount, type_, category, date, description):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO expenses 
           (user_id, amount, type, category, date, description)
           VALUES (%s,%s,%s,%s,%s,%s)""",
        (user_id, amount, type_, category, date, description)
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_transactions(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """SELECT date, category, amount, type 
           FROM expenses 
           WHERE user_id=%s 
           ORDER BY date DESC""",
        (user_id,)
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
