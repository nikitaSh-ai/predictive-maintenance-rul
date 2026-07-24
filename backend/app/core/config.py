"""
config.py

Centralized application configuration.
"""

import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "Predictive Maintenance AI"
)

MODEL_VERSION = os.getenv(
    "MODEL_VERSION",
    "Version2"
)

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER",
    "uploads"
)

MAX_UPLOAD_SIZE_MB = int(
    os.getenv(
        "MAX_UPLOAD_SIZE_MB",
        "20"
    )
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)