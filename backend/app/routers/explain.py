from fastapi import APIRouter
from backend.app.services.prediction_service import (
    get_latest_prediction,
)
router = APIRouter()
@router.get("/explain")
def explain(engine_id: int = None):
    prediction = get_latest_prediction(engine_id)

    feature_importance = prediction.get(
        "feature_importance",
        {},
    )

    if isinstance(feature_importance, list):
        feature_importance = {
            item["feature"]: item["importance"]
            for item in feature_importance
        }

    return {
        "feature_importance": feature_importance,
    }