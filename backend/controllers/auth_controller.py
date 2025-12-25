# auth_controller.py
# Handles Flask routes for authentication: login, register, logout

from flask import Blueprint, render_template, request, redirect, url_for, session
from backend.services.auth_service import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    """
    Route to register a new user
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        result = register_user(username, email, password)
        if result['success']:
            return redirect(url_for('auth_bp.login'))
        return render_template('register.html', error=result['message'])
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    """
    Route to login a user
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = login_user(email, password)
        if result['success']:
            session['user_id'] = result['user']['id']
            session['username'] = result['user']['username']
            return redirect(url_for('dashboard_bp.dashboard'))
        return render_template('login.html', error=result['message'])
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    """
    Clears session to logout user
    """
    session.clear()
    return redirect(url_for('auth_bp.login'))
