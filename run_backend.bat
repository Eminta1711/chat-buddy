@echo off
REM Start the Calm Chat backend
REM Make sure you have activated the virtual environment first

echo.
echo 🌿 Starting Calm Chat Backend...
echo.

cd /d "%~dp0"
python main.py

pause
