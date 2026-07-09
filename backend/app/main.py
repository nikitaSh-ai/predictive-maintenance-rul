import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2].parent
sys.path.append(str(PROJECT_ROOT))



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers.predict import router as predict_router


app = FastAPI(

    title="Predictive Maintenance API",

    description="Backend API for Remaining Useful Life Prediction",

    version="1.0.0",

)

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


@app.get("/")
def root():

    return {

        "message": "Predictive Maintenance API is running."

    }