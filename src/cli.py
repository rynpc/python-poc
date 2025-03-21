"""
Command-line interface for the Task Manager application.

This module provides a menu-driven interface for:
- Adding new tasks
- Listing all tasks
- Marking tasks as completed
- Deleting tasks

The interface is user-friendly and handles input validation.
"""

from datetime import datetime
from typing import Optional

from .task_manager import TaskManager, Task

def print_task(task: Task) -> None:
    """
    Print a task's details in a formatted way.

    Args:
        task: The task to print
    """
    status = "✓" if task.completed else " "
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
    print(f"\n[{status}] Task {task.id}: {task.title}")
    print(f"Description: {task.description}")
    print(f"Due date: {due_date}")

def parse_date(date_str: str) -> Optional[datetime]:
    """
    Parse a date string into a datetime object.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        Parsed datetime object or None if the string is empty
    """
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return None

def add_task(manager: TaskManager) -> None:
    """
    Add a new task through user input.

    Args:
        manager: The task manager instance
    """
    print("\nAdd a new task:")
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    date_str = input("Due date (YYYY-MM-DD, or press Enter to skip): ").strip()

    due_date = parse_date(date_str)
    if due_date is None and date_str:
        return

    try:
        task = manager.add_task(title, description, due_date)
        print("\nTask added successfully!")
        print_task(task)
    except ValueError as e:
        print(f"\nError: {e}")

def list_tasks(manager: TaskManager) -> None:
    """
    List all tasks in the manager.

    Args:
        manager: The task manager instance
    """
    include_completed = input("\nInclude completed tasks? (y/N): ").lower() == 'y'
    tasks = manager.list_tasks(include_completed)

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nTasks:")
    for task in tasks:
        print_task(task)

def mark_completed(manager: TaskManager) -> None:
    """
    Mark a task as completed through user input.

    Args:
        manager: The task manager instance
    """
    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))
        task = manager.mark_completed(task_id)
        print("\nTask marked as completed:")
        print_task(task)
    except ValueError:
        print("\nError: Invalid task ID")
    except KeyError as e:
        print(f"\nError: {e}")

def delete_task(manager: TaskManager) -> None:
    """
    Delete a task through user input.

    Args:
        manager: The task manager instance
    """
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        manager.delete_task(task_id)
        print("\nTask deleted successfully!")
    except ValueError:
        print("\nError: Invalid task ID")
    except KeyError as e:
        print(f"\nError: {e}")

def print_menu() -> None:
    """Print the main menu options."""
    print("\nTask Manager Menu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def main() -> None:
    """Main entry point for the CLI application."""
    manager = TaskManager()
    actions = {
        "1": add_task,
        "2": list_tasks,
        "3": mark_completed,
        "4": delete_task
    }

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 