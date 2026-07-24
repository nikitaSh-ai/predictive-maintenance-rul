@echo off

cd /d "%~dp0"

echo ============================================
echo Starting Backend...
echo ============================================

call backend\venv\Scripts\activate.bat

uvicorn backend.app.main:app --reload

pause