# Simple Task Manager

A simple command-line task manager application that demonstrates Python best practices and testability.

## Features

- Add tasks with title, description, and optional due date
- List all tasks or only incomplete tasks
- Mark tasks as completed
- Delete tasks
- Full unit test coverage with HTML reports

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI application:
```bash
python cli.py
```

The application will present a menu with the following options:
1. Add task
2. List tasks
3. Mark task as completed
4. Delete task
5. Exit

## Running Tests

There are several ways to run the tests:

### Basic unittest runner
```bash
python -m unittest test_task_manager.py
```

### Using pytest with coverage
```bash
pytest
```
This will:
- Run all tests
- Generate a terminal coverage report
- Create an HTML coverage report in the `htmlcov` directory

To view the HTML coverage report, open `htmlcov/index.html` in your web browser.

### IDE Integration

Most Python IDEs (like PyCharm, VS Code) support pytest integration:
- VS Code: Install the Python extension and click the "Run Test" button above any test
- PyCharm: Click the green "Run" button next to any test

The coverage report will help you identify:
- Which lines of code are executed during tests
- Which lines are missing test coverage
- Overall coverage percentage for each file

## Project Structure

- `task_manager.py`: Core task management functionality
- `cli.py`: Command-line interface
- `test_task_manager.py`: Unit tests
- `requirements.txt`: Project dependencies
- `pytest.ini`: Test configuration
- `htmlcov/`: Generated coverage reports (after running tests) 
