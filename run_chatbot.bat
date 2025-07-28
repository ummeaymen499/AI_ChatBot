@echo off
REM ChatBot Application Launcher for Windows

echo ========================================
echo ChatBot Application Launcher
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "main.py" (
    echo ERROR: main.py not found
    echo Please run this script from the ChatBot project directory
    pause
    exit /b 1
)

REM Install dependencies if needed
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Choose an option:
echo 1. Run Web Interface (Default)
echo 2. Run CLI Interface
echo 3. Run Tests
echo 4. Build Docker Image
echo.

set /p choice="Enter your choice (1-4, default is 1): "

if "%choice%"=="2" (
    echo Starting CLI interface...
    python main.py cli
) else if "%choice%"=="3" (
    echo Running tests...
    python test_chatbot.py
) else if "%choice%"=="4" (
    echo Building Docker image...
    docker build -t chatbot-app .
    echo Docker image built successfully!
    echo To run: docker run -p 5000:5000 chatbot-app
) else (
    echo Starting web interface...
    echo.
    echo ChatBot will be available at: http://localhost:5000
    echo Press Ctrl+C to stop the server
    echo.
    python main.py
)

pause
