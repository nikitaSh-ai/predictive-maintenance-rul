from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import sys
import logging
from pathlib import Path
from backend.app.routers import version2
from backend.app.database.database import initialize_database

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_DIST = PROJECT_ROOT / "frontend" / "dist"
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
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router)
app.include_router(explain_router)
app.include_router(uncertainty_router)
app.include_router(
    version2.router
)

if FRONTEND_DIST.exists():
    app.mount(
        "/assets",
        StaticFiles(directory=FRONTEND_DIST / "assets"),
        name="assets",
    )

@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_DIST / "index.html")



@app.get("/{full_path:path}")
def catch_all(full_path: str):
    file_path = FRONTEND_DIST / full_path

    if file_path.exists() and file_path.is_file():
        return FileResponse(file_path)

    return FileResponse(FRONTEND_DIST / "index.html")