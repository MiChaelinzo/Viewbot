@echo off
echo ============================================================
echo Multi-Platform View Bot Launcher
echo ============================================================
echo.
echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)
echo.
echo Installing/Updating dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo ============================================================
echo Starting the bot...
echo ============================================================
echo.
python youtube_refresher.py
pause

