@echo off
title Driving Test Application
echo Starting Driving Test Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "index.html" (
    echo ERROR: index.html not found!
    echo Make sure this batch file is in the same folder as index.html
    echo.
    pause
    exit /b 1
)

if not exist "pytania.csv" (
    echo ERROR: pytania.csv not found!
    echo Make sure pytania.csv is in the same folder as this batch file
    echo.
    pause
    exit /b 1
)

echo Files found! Starting server...
echo.
echo The application will open in your browser automatically.
echo To stop the server, close this window or press Ctrl+C
echo.
echo Starting...

REM Start the Python server
python start_app.py

echo.
echo Server stopped.
pause 