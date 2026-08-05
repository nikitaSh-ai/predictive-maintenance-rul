@echo off
title Predictive Maintenance System

REM Move to the folder where this BAT file is located
cd /d "%~dp0"

echo =====================================
echo Starting Predictive Maintenance System...
echo =====================================

call backend\venv\Scripts\activate.bat

set PYTHONPATH=%CD%

start "Backend" cmd /k "uvicorn backend.app.main:app --reload"

timeout /t 5 > nul

start "" http://127.0.0.1:8000