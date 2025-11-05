@echo off
echo ======================================
echo   wirefish setup and launch script
echo ======================================

python -m pip install --upgrade pip

echo installing libraries from requirements.txt...
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] installation failed.
    echo make sure you have python installed
    pause
    exit /b
)

echo.
echo Launching Wirefish...
python ./src/main.py

pause