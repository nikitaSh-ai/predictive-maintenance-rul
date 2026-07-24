"""
prediction_service.py

Store the latest prediction results
for dashboard pages.
"""
from backend.app.database.database import get_connection
LATEST_PREDICTION = {}


def save_prediction(prediction):
    """
    Save the latest prediction
    and store it in the database.
    """

    global LATEST_PREDICTION

    LATEST_PREDICTION = prediction

    save_prediction_to_database(
        prediction
    )


def get_latest_prediction():
    """
    Return the latest prediction.
    """

    return LATEST_PREDICTION





def get_prediction_history():
    """
    Return all saved predictions.
    """

    connection = get_connection()

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT *
        FROM prediction_history
        ORDER BY prediction_time DESC
        """
    ).fetchall()

    connection.close()

    return [
        dict(row)
        for row in rows
    ]






def save_prediction_to_database(prediction):
    """
    Store prediction permanently in SQLite.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            engine_id,
            predicted_rul,
            risk,
            confidence,
            recommendation
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            prediction["engine_id"],
            prediction["predicted_rul"],
            prediction["risk"],
            prediction["confidence"],
            prediction["recommendation"],
        ),
    )

    connection.commit()

    connection.close()