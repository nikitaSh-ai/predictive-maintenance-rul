from fastapi import HTTPException
import pandas as pd
import os







        
class InputValidator:
    """
    Validate uploaded NASA dataset before prediction.
    """


    @staticmethod
    def validate(file_path: str):

        # -----------------------------
        # File Extension Validation
        # -----------------------------

        allowed_extensions = [".csv", ".txt"]

        extension = os.path.splitext(file_path)[1].lower()

        if extension not in allowed_extensions:

            raise HTTPException(
                status_code=400,
                detail="Only CSV and TXT files are supported."
            )