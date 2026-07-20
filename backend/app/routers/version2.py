import os
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile


from src.pipeline.predict_engine_v2 import (
    run_prediction_v2,
)
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

        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(
            upload_dir,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = run_prediction_v2(file_path)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )