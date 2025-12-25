# backend/db.py
# MySQL connection using mysql-connector-python

import mysql.connector
from mysql.connector import pooling
from backend.config import Config

# Create a connection pool (efficient & safe)
db_pool = pooling.MySQLConnectionPool(
    pool_name="nexa_pool",
    pool_size=5,
    host=Config.MYSQL_HOST,
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PASSWORD,
    database=Config.MYSQL_DB,
    port=Config.MYSQL_PORT,
    charset="utf8mb4"
)

def get_db():
    """
    Get a database connection from the pool
    """
    return db_pool.get_connection()
