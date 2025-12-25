# transaction_controller.py
# Handles Flask routes for expenses/income page

from flask import Blueprint, render_template, request, session, redirect, url_for
from backend.services.transaction_service import add_transaction, get_transactions

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))

    user_id = session['user_id']

    if request.method == 'POST':
        amount = float(request.form['amount'])
        type_ = request.form['type']
        category = request.form['category']
        date = request.form['date']
        description = request.form['description']

        add_transaction(user_id, amount, type_, category, date, description)

    transactions = get_transactions(user_id)
    return render_template('expenses.html', transactions=transactions)
