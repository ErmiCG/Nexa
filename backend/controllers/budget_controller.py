# budget_controller.py
# Handles Flask routes for budget page

from flask import Blueprint, render_template, request, session, redirect
from backend.services.budget_service import set_budget, get_budget_status

budget_bp = Blueprint('budget_bp', __name__)

@budget_bp.route('/budget', methods=['GET','POST'])
def budget():
    """
    Set and display user's budget and progress
    """
    if 'user_id' not in session:
        return redirect('/login')
    user_id = session['user_id']

    if request.method == 'POST':
        month = request.form['month']
        amount = float(request.form['amount'])
        set_budget(user_id, month, amount)

    data = get_budget_status(user_id)
    return render_template('budget.html',
                           total_budget=data['total_budget'],
                           spent=data['spent'],
                           remaining=data['remaining'],
                           progress=data['progress'])
