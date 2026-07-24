"""
database.py

Purpose:
Create and manage the SQLite database connection.
"""

import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).parent
    / "prediction_history.db"
)


def get_connection():
    """
    Return a SQLite connection.
    """

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection









def initialize_database():
    """
    Create required database tables.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prediction_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            engine_id INTEGER NOT NULL,

            predicted_rul REAL NOT NULL,

            risk TEXT NOT NULL,

            confidence TEXT NOT NULL,

            recommendation TEXT NOT NULL,

            prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    connection.commit()

    connection.close()