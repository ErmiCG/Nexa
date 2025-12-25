# reports_controller.py
from flask import Blueprint, render_template, session, redirect, url_for
from backend.services.dashboard_service import get_dashboard_data

reports_bp = Blueprint('reports_bp', __name__, url_prefix='/reports')

@reports_bp.route('/')
def reports():
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))

    user_id = session['user_id']
    data = get_dashboard_data(user_id)

    return render_template(
        'reports.html',
        monthly_income=data['monthly_income'],
        today_expense=data['today_expense'],
        saving_progress=data['saving_progress']
    )
