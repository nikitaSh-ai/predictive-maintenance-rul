from fastapi import APIRouter

import backend.app.services.explainability_service as explain_service

router = APIRouter()


@router.get("/explain")
def explain():

   return {
    "feature_importance": explain_service.LATEST_EXPLANATION
}