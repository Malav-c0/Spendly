import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "spendly.db"


def get_db():
    """Open a connection to the SQLite database with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create the database tables if they do not already exist."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """Insert demo data if not already present."""
    conn = get_db()
    cursor = conn.cursor()

    # Check if users table already has data
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # Insert demo user
    demo_password_hash = generate_password_hash("demo123")
    cursor.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", demo_password_hash)
    )

    # Get the demo user's ID
    cursor.execute("SELECT id FROM users WHERE email = ?", ("demo@spendly.com",))
    demo_user_id = cursor.fetchone()[0]

    # Insert 8 sample expenses across all categories
    # Categories: Food, Transport, Bills, Health, Entertainment, Shopping, Other
    sample_expenses = [
        (demo_user_id, 15.50, "Food", "2026-04-01", "Lunch at cafe"),
        (demo_user_id, 25.00, "Transport", "2026-04-03", "Uber ride"),
        (demo_user_id, 120.00, "Bills", "2026-04-05", "Electric bill"),
        (demo_user_id, 45.00, "Health", "2026-04-07", "Pharmacy"),
        (demo_user_id, 30.00, "Entertainment", "2026-04-10", "Movie tickets"),
        (demo_user_id, 85.00, "Shopping", "2026-04-12", "New shoes"),
        (demo_user_id, 20.00, "Other", "2026-04-15", "Miscellaneous"),
        (demo_user_id, 42.00, "Food", "2026-04-18", "Dinner with friends"),
    ]

    cursor.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        sample_expenses
    )

    conn.commit()
    conn.close()
