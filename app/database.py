import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "api_health.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS api_checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                reachable INTEGER NOT NULL,
                healthy INTEGER NOT NULL,
                status_code INTEGER,
                response_time_ms REAL NOT NULL,
                error TEXT,
                checked_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()

    finally:
        connection.close()


def save_api_check(result):
    connection = get_connection()

    try:
        connection.execute("""
            INSERT INTO api_checks (
                url,
                reachable,
                healthy,
                status_code,
                response_time_ms,
                error
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            result["url"],
            result["reachable"],
            result["healthy"],
            result["status_code"],
            result["response_time_ms"],
            result["error"]
        ))

        connection.commit()

    finally:
        connection.close()

def get_api_check_history():
    connection = get_connection()

    try:
        records = connection.execute("""
            SELECT *
            FROM api_checks
            ORDER BY checked_at DESC, id DESC
        """).fetchall()

        return [dict(record) for record in records]

    finally:
        connection.close()