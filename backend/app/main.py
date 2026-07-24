import sys
import logging
from pathlib import Path
from backend.app.routers import version2
from backend.app.database.database import initialize_database

PROJECT_ROOT = Path(__file__).resolve().parents[2].parent
sys.path.append(str(PROJECT_ROOT))


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers.uncertainty import (
    router as uncertainty_router
)
from backend.app.routers.predict import router as predict_router
from backend.app.routers.explain import router as explain_router



app = FastAPI(

    title="Predictive Maintenance API",

    description="Backend API for Remaining Useful Life Prediction",

    version="1.0.0",

)

initialize_database()

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

app.include_router(predict_router)
app.include_router(explain_router)
app.include_router(uncertainty_router)
app.include_router(
    version2.router
)

@app.get("/")
def root():

    return {

        "message": "Predictive Maintenance API is running."

    }