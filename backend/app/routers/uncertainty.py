from fastapi import APIRouter

from backend.app.services.prediction_service import (
    get_latest_prediction,
)

router = APIRouter()


@router.get("/uncertainty")
def get_uncertainty():

    prediction = get_latest_prediction()

    return {

        "confidence": prediction.get("confidence"),

        "uncertainty": prediction.get("uncertainty"),

        "mc_mean": prediction.get("mc_mean"),

        "mc_samples": prediction.get("mc_samples"),

        "predicted_rul": prediction.get("predicted_rul"),

        "risk": prediction.get("risk"),

    }