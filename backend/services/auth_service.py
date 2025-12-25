# auth_service.py
# Handles authentication logic: registration and login
from backend.db import get_db  # Use your connection pool
from werkzeug.security import generate_password_hash, check_password_hash
import re

def register_user(username, email, password):
    """
    Registers a new user in the database
    - Password must be at least 8 chars, include 1 uppercase, 1 number
    - Returns a dict with success status and message
    """
    # Password validation
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
        return {'success': False, 'message': 'Password must be at least 8 chars, include 1 uppercase letter and 1 number'}

    conn = get_db()        # Get connection from pool
    cursor = conn.cursor()

    try:
        # Check if email already exists
        cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
        if cursor.fetchone():
            return {'success': False, 'message': 'Email already exists'}

        # Hash password and insert user
        hashed_password = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        conn.commit()
        return {'success': True, 'message': 'User registered successfully'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    finally:
        cursor.close()
        conn.close()


def login_user(email, password):
    """
    Logs in a user by checking email and password
    Returns user data if success, else error message
    """
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, username, email, password FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user[3], password):
            return {'success': True, 'user': {'id': user[0], 'username': user[1]}}
        return {'success': False, 'message': 'Invalid credentials'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    finally:
        cursor.close()
        conn.close()
