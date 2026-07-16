"""
prediction_service.py

Store the latest prediction results
for dashboard pages.
"""

LATEST_PREDICTION = {}


def save_prediction(prediction):
    """
    Save the latest prediction.
    """

    global LATEST_PREDICTION

    LATEST_PREDICTION = prediction


def get_latest_prediction():
    """
    Return the latest prediction.
    """

    return LATEST_PREDICTION