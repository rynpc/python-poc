#!/bin/bash
set -e

# Run tests with coverage
echo "Running tests with coverage..."
pytest --cov=src --cov-report=html --cov-report=xml

# Check code formatting with Black
echo "Checking code formatting with Black..."
black --check src tests

# Check import ordering with isort
echo "Checking import ordering with isort..."
isort --check-only src tests

# Run linting with Flake8
echo "Running linting with Flake8..."
flake8 src tests

# Run type checking with MyPy
echo "Running type checking with MyPy..."
mypy src tests

# Run security checks with Safety
echo "Running security checks with Safety..."
safety scan --full-report

# Run security checks with Bandit
echo "Running security checks with Bandit..."
bandit -r src -x tests

# Check documentation coverage with pydocstyle
echo "Checking documentation coverage with pydocstyle..."
pydocstyle src