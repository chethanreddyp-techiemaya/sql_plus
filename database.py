import sqlite3


def get_db_connection():
    conn = sqlite3.connect("employees.db")  # SQLite database file
    conn.row_factory = sqlite3.Row  # Optional: enables dict-like access
    return conn