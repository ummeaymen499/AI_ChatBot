#!/bin/bash

# ChatBot Application Launcher for Unix-like systems

echo "========================================"
echo "ChatBot Application Launcher"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "ERROR: main.py not found"
    echo "Please run this script from the ChatBot project directory"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Choose an option:"
echo "1. Run Web Interface (Default)"
echo "2. Run CLI Interface"
echo "3. Run Tests"
echo "4. Build Docker Image"
echo ""

read -p "Enter your choice (1-4, default is 1): " choice

case $choice in
    2)
        echo "Starting CLI interface..."
        python main.py cli
        ;;
    3)
        echo "Running tests..."
        python test_chatbot.py
        ;;
    4)
        echo "Building Docker image..."
        docker build -t chatbot-app .
        echo "Docker image built successfully!"
        echo "To run: docker run -p 5000:5000 chatbot-app"
        ;;
    *)
        echo "Starting web interface..."
        echo ""
        echo "ChatBot will be available at: http://localhost:5000"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python main.py
        ;;
esac
