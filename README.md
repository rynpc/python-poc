# Simple Task Manager

A simple command-line task manager application that demonstrates Python best practices and testability.

## Features

- Add tasks with title, description, and optional due date
- List all tasks or only incomplete tasks
- Mark tasks as completed
- Delete tasks
- Full unit test coverage with HTML reports

## Project Structure

```
python-poc/
├── src/                    # Source code
│   ├── task_manager.py    # Core task management functionality
│   └── cli.py            # Command-line interface
├── tests/                 # Test files
│   └── test_task_manager.py
├── scripts/              # Development scripts
│   ├── setup.sh         # Setup development environment
│   └── teardown.sh      # Clean up development environment
├── requirements.txt      # Project dependencies
├── pytest.ini           # Test configuration
└── README.md            # This file
```

## Quick Start

1. Clone this repository
2. Run the setup script:
   ```bash
   # On macOS/Linux:
   ./scripts/setup.sh
   
   # On Windows (using Git Bash or WSL):
   ./scripts/setup.sh
   ```
   This will:
   - Create a virtual environment
   - Install dependencies
   - Run the tests to verify everything is working

## Development

### Running Tests
```bash
# Basic test run
pytest

# Run tests with coverage report
pytest --cov=. --cov-report=term-missing
```

### IDE Integration
- **Cursor IDE**: Open the integrated terminal (Cmd/Ctrl + `), ensure you're in the project directory, and run `pytest`
- **VS Code**: Install the Python extension and click the "Run Test" button above any test
- **PyCharm**: Click the green "Run" button next to any test

### Clean Up
When you're done developing or want to start fresh:
```bash
./scripts/teardown.sh
```
This will clean up the virtual environment, cache files, and coverage reports.

## Usage

Run the CLI application:
```bash
python src/cli.py
```

The application will present a menu with the following options:
1. Add task
2. List tasks
3. Mark task as completed
4. Delete task
5. Exit

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests: `pytest`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
