# Nexa - Personal Finance Management

## Features
- User registration and login with strong password validation
- Dashboard showing today's expenses, monthly income, budget used, savings
- Track expenses and incomes with category, description, and date
- Set monthly budgets and track progress
- Create saving goals with progress tracking
- Persistent user-specific data in MySQL
- Logout functionality
- Responsive design with dark-blue Elliot Alderso theme and animations

## Installation
1. Clone repository
2. Install Python dependencies: `pip install flask flask-mysqldb werkzeug`
3. Setup MySQL database:
   - Run `schema.sql`
   - Update `config.py` with MySQL credentials
4. Run application:
```bash
python backend/app.py
