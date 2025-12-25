# app.py
# Main entry point for Nexa Flask application

import os
from flask import Flask, redirect, url_for

# Import blueprints
from backend.controllers.auth_controller import auth_bp
from backend.controllers.dashboard_controller import dashboard_bp
from backend.controllers.transaction_controller import transaction_bp
from backend.controllers.budget_controller import budget_bp
from backend.controllers.goal_controller import goal_bp
from backend.controllers.reports_controller import reports_bp

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '../frontend/templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '../frontend/static')
    )
    app.secret_key = "supersecretkey"

    @app.route('/')
    def home():
        return redirect(url_for('auth_bp.login'))


    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(budget_bp)
    app.register_blueprint(goal_bp)
    app.register_blueprint(reports_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
