# Nexa - Your Smart Assistant
Nexa is a modern, responsive personal finance management web application built with 
Flask and MySQL. It helps users track expenses, manage budgets, set savings goals,
and view financial reports in a clean, tech-style dashboard.
## Features
- User registration and login with session-based authentication
- Personal dashboard with key financial metrics
- Add and track expenses and income
- Monthly budget management with progress tracking
- Savings goals with visual progress bars
- Reports page with animated bar and pie charts (user-specific data)
- Persistent data storage using MySQL
- Responsive UI (desktop & mobile friendly)
- Modern dark-themed design with animations
# Tech Stack
- Backend: Python (Flask)
- Database: MySQL (MySQL Connector)
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js

## Installation
1. Clone repository
2. Create and activate a virtual environment (optional but recommended)
3. Install Python dependencies: `pip install flask mysql.connector.python`
4. Setup MySQL database:
   - Start MySQL (XAMPP recommended)
   - Create a database
   - Run the provided SQL schema file
   - Update database credentials in config.py
5. Run application:
bash --- python backend/app.py or python -m backend.app on cmd or terminal
6. Open in browser:
- http://127.0.0.1:5000
# Demo Account
- Email: alice@example.com or use demo@nexa.com
- Password: Password123 for alice and Demo1234 for the demo
# Project Structure
- backend/ – Flask app, controllers, services, database logic
- templates/ – HTML pages
- static/ – CSS, JavaScript, assets
- schema.sql – Database structure
# Notes
- All data is user-specific and securely stored
- Charts and progress bars update dynamically based on user data
- Designed for learning, academic projects, and portfolio use



