#!/bin/bash

# Exit on error
set -e

echo "🚀 Setting up Python Task Manager project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run tests
echo "🧪 Running tests..."
pytest

echo "✅ Setup complete! Your virtual environment is activated and ready to use."
echo "To deactivate the virtual environment when you're done, run: deactivate" 