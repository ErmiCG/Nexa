-- Drop old database if it exists
DROP DATABASE IF EXISTS nexa_db;

-- Create a new database
CREATE DATABASE nexa_db;
USE nexa_db;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(120) UNIQUE,
    password VARCHAR(255)
);

-- Create expenses table
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount FLOAT,
    type VARCHAR(10),
    category VARCHAR(50),
    date DATE,
    description VARCHAR(255),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create budgets table
CREATE TABLE budgets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    month VARCHAR(20),
    amount FLOAT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create goals table
CREATE TABLE goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    target_amount FLOAT,
    current_amount FLOAT DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert sample user
INSERT INTO users (username, email, password)
VALUES ('Demo User','demo@nexa.com','$2b$12$C9xj5N8lGQFf6O1Q3LzA2u1aU8JQ1G2vF/RcP92U6fBn7ZzR6aX9e');

-- Insert sample expenses
INSERT INTO expenses (user_id, amount, type, category, date, description)
VALUES 
(1, 1500, 'Income', 'Salary', '2025-12-01', 'Monthly salary'),
(1, 200, 'Expense', 'Food', '2025-12-02', 'Groceries'),
(1, 50, 'Expense', 'Transport', '2025-12-03', 'Bus fare');

-- Insert sample budgets
INSERT INTO budgets (user_id, month, amount)
VALUES (1, 'December', 2000);

-- Insert sample goals
INSERT INTO goals (user_id, name, target_amount, current_amount)
VALUES
(1, 'New Laptop', 1500, 200),
(1, 'Vacation', 1000, 300);
