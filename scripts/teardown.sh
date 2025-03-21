#!/bin/bash

# Exit on error
set -e

echo "🧹 Cleaning up Python Task Manager project..."

# Deactivate virtual environment if it's active
if [ -n "$VIRTUAL_ENV" ]; then
    echo "🔌 Deactivating virtual environment..."
    type deactivate >/dev/null 2>&1 && deactivate || true
fi

# Remove virtual environment
if [ -d "venv" ]; then
    echo "🗑️ Removing virtual environment..."
    rm -rf venv
fi

# Remove Python cache files
echo "🧹 Removing Python cache files..."
find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete

# Remove coverage reports
if [ -d "htmlcov" ]; then
    echo "🗑️ Removing coverage reports..."
    rm -rf htmlcov
fi

# Remove pytest cache
if [ -d ".pytest_cache" ]; then
    echo "🗑️ Removing pytest cache..."
    rm -rf .pytest_cache
fi

# Remove coverage data
rm -f .coverage coverage.xml

echo "✅ Cleanup complete! Project is ready for a fresh setup." 