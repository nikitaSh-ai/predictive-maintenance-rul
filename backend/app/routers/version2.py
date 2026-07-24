import os
import logging
import shutil
from backend.app.utils.input_validator import InputValidator
from fastapi import APIRouter, File, HTTPException, UploadFile
from backend.app.core.config import UPLOAD_FOLDER
from backend.app.services.prediction_service import (
    get_prediction_history,
)


from src.pipeline.predict_engine_v2 import (
    run_prediction_v2,
)


logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/version2",
    tags=["Version 2"]
)


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Version 2 prediction endpoint.
    """

    try:

        upload_dir = UPLOAD_FOLDER
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(
            upload_dir,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        InputValidator.validate(file_path)

        result = run_prediction_v2(file_path)

        return result

    except ValueError as e:

        raise HTTPException(
        status_code=400,
        detail=str(e)
    )

    except Exception as e:

      logger.exception(
        "Unexpected error during prediction."
       )

      raise 



@router.get("/history")
def prediction_history():
    """
    Return prediction history.
    """

    return {
        "history": get_prediction_history()
    }
