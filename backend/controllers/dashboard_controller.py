# dashboard_controller.py
# Handles dashboard route

from flask import Blueprint, render_template, session, redirect, url_for
from backend.services.dashboard_service import get_dashboard_data

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard')


@dashboard_bp.route('/dashboard')
def dashboard():
    """
    Renders dashboard for logged-in user
    """
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))
    
    user_id = session['user_id']
    data = get_dashboard_data(user_id)

    return render_template('dashboard.html',
                           today_expense=data['today_expense'],
                           monthly_income=data['monthly_income'],
                           budget_used=data['budget_used'],
                           saving_progress=data['saving_progress'])
