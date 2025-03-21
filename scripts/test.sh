#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html -v

# Open coverage report in browser
if [[ "$OSTYPE" == "darwin"* ]]; then
    open htmlcov/index.html
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open htmlcov/index.html
fi 