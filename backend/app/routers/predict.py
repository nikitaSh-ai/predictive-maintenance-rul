from backend.app.services.model_service import MODEL_DIR

import pandas as pd

import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import tempfile

from src.pipeline.predict_engine import run_prediction

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check file extension
    if not (
        file.filename.endswith(".txt")
        or file.filename.endswith(".csv")
    ):
        raise HTTPException(
            status_code=400,
            detail="Only CSV and TXT files are allowed."
        )

    with tempfile.NamedTemporaryFile(
    delete=False,
    suffix=os.path.splitext(file.filename)[1]
    ) as temp_file:

      temp_file.write(await file.read())

      temp_path = temp_file.name




    try:

      result = run_prediction(temp_path)

      return result

    except ValueError as error:

       raise HTTPException(
        status_code=400,
        detail=str(error)
      )

    except Exception as error:

      logger.exception("Prediction failed.")

      raise HTTPException(
        status_code=500,
        detail="Prediction failed due to an internal error."
       )

    finally:

      os.remove(temp_path)