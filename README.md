# Task Manager

A simple command-line task management application built with Python, featuring automated test coverage reporting.

[![Coverage](https://img.shields.io/badge/coverage-38%25-brightgreen.svg)](https://rynpc.github.io/python-poc/)

## Features

- Add tasks with title, description, and optional due date
- List all tasks or filter by completion status
- Mark tasks as completed
- Delete tasks
- Update task details
- Input validation and error handling
- Automated test coverage reporting
- GitHub Actions integration for CI/CD
- CodeQL security scanning

## Project Structure

```
python-poc/
├── src/                     # Source code
│   ├── task_manager.py      # Core task management functionality
│   ├── cli.py               # Command-line interface
│   └── coverage_utils/      # Coverage reporting utilities
│       └── get_coverage.py  # Coverage badge updater
├── tests/                   # Test files
│   ├── test_task_manager.py
│   └── test_get_coverage.py
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       ├── pipeline.yml     # CI/CD pipeline workflow
│       ├── deploy-coverage.yml  # Coverage reporting workflow
│       └── codeql.yml       # Security scanning workflow
├── scripts/                 # Development scripts
│   ├── setup.sh             # Initialize development environment
│   ├── test.sh              # Run tests with coverage
│   └── run.sh               # Run the application
├── htmlcov/                 # HTML coverage reports
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
├── pytest.ini               # Pytest configuration
├── coverage.xml             # XML coverage report
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
python -m pytest tests/ --cov=src --cov-report=html --cov-report=xml
```

### Code Coverage

Test coverage is automatically tracked and reported:
- Coverage badge in README is updated automatically via GitHub Actions
- Coverage reports are deployed to GitHub Pages
- View detailed coverage report at: [https://rynpc.github.io/python-poc/](https://rynpc.github.io/python-poc/)

### GitHub Actions Workflows

## CI/CD Pipeline Status

⚠️ **The CI/CD pipeline is currently disabled.**  
The workflow in `.github/workflows/pipeline.yml` has been commented out due to repeated job failures and lack of time to update it at the moment.  
Once fixes and improvements are made, the pipeline will be restored.


The project uses GitHub Actions for automation:
- **Coverage Reporting**: Runs tests and updates coverage badge
- **CodeQL Analysis**: Security scanning for code vulnerabilities
- **Environment Protection**: Ensures code quality and security before deployment

## Dependencies

- Python 3.x
- pytest >= 7.4.0
- pytest-cov >= 4.1.0
- python-dateutil >= 2.8.2
- flake8 >= 6.1.0

## License

MIT License
