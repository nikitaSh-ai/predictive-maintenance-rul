"""
prediction_service.py

Store the latest prediction results
for dashboard pages.
"""
from backend.app.database.database import get_connection

PREDICTIONS_BY_ENGINE = {}
LATEST_ENGINE_ID = None

def save_prediction(prediction):
    """
    Save the prediction for its specific engine,
    and store it in the database.
    """
    global LATEST_ENGINE_ID

    PREDICTIONS_BY_ENGINE[prediction["engine_id"]] = prediction
    LATEST_ENGINE_ID = prediction["engine_id"]

    save_prediction_to_database(
        prediction
    )

def get_latest_prediction(engine_id=None):
    """
    Return the prediction for a specific engine_id
    if provided, otherwise the most recently
    processed engine's prediction.
    """

    if engine_id is not None:
        return PREDICTIONS_BY_ENGINE.get(engine_id, {})

    if LATEST_ENGINE_ID is None:
        return {}

    return PREDICTIONS_BY_ENGINE.get(LATEST_ENGINE_ID, {})



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