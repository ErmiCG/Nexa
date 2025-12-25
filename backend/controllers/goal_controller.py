# goal_controller.py
# Handles Flask routes for goals page

from flask import Blueprint, render_template, request, session, redirect
from backend.services.goal_service import add_savings, create_goal, get_goals

goal_bp = Blueprint('goal_bp', __name__)

@goal_bp.route('/goals', methods=['GET','POST'])
def goals():
    """
    Create new goal and display active goals
    """
    if 'user_id' not in session:
        return redirect('/login')
    user_id = session['user_id']

    if request.method == 'POST':
        name = request.form['name']
        target = float(request.form['target'])
        create_goal(user_id, name, target)

    goals_list = get_goals(user_id)
    return render_template('goals.html', goals=goals_list)
@goal_bp.route('/goals/save', methods=['POST'])
def save_goal():
    goal_id = request.form['goal_id']
    amount = float(request.form['amount'])
    add_savings(goal_id, amount)
    return redirect('/goals')
