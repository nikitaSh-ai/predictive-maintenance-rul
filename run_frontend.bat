@echo off

cd /d "%~dp0"

echo ============================================
echo Starting Frontend...
echo ============================================

cd frontend

npm run dev

pause