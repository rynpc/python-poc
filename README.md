# Task Manager

A simple command-line task management application built with Python.

[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen.svg)](https://ryancowan.github.io/python-poc/coverage/) [View Coverage Report](https://ryancowan.github.io/python-poc/coverage/)

## Features

- Add tasks with title, description, and optional due date
- List all tasks or filter by completion status
- Mark tasks as completed
- Delete tasks
- Update task details
- Input validation and error handling

## Project Structure

```
python-poc/
├── src/                    # Source code
│   ├── task_manager.py    # Core task management functionality
│   └── cli.py            # Command-line interface
├── tests/                 # Test files
│   └── test_task_manager.py
├── scripts/              # Development scripts
│   ├── setup.sh         # Initialize development environment
│   ├── test.sh          # Run tests with coverage
│   └── run.sh           # Run the application
├── requirements.txt       # Project dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-poc
```

2. Run the setup script:
```bash
./scripts/setup.sh
```

Or manually:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
./scripts/run.sh
```

Or manually:
```bash
python src/cli.py
```

### Menu Options

1. **Add task**: Create a new task with title, description, and optional due date
2. **List tasks**: View all tasks or filter by completion status
3. **Mark task as completed**: Mark a task as done
4. **Delete task**: Remove a task from the list
5. **Exit**: Close the application

## Development

### Running Tests

```bash
./scripts/test.sh
```

Or manually:
```bash
python -m pytest tests/ -v
```

### Code Coverage

The test script automatically generates and opens a coverage report in your browser. You can also generate it manually:
```bash
python -m pytest tests/ --cov=src --cov-report=html
```

## Dependencies

- Python 3.9+
- pytest
- pytest-cov
- datetime

## License

MIT License 