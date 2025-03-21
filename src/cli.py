"""
Command Line Interface for Task Manager

This module provides a command-line interface for interacting with the TaskManager.
It offers a menu-driven interface for adding, listing, completing, and deleting tasks.
"""

from datetime import datetime
from typing import Optional
from task_manager import TaskManager, Task

def print_task(task: Task) -> None:
    """Print a task's details in a formatted way.
    
    Args:
        task: The Task object to print
    """
    status = "✓" if task.completed else " "
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
    print(f"[{status}] Task {task.id}: {task.title}")
    print(f"    Description: {task.description}")
    print(f"    Due date: {due_date}")
    print()

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse a date string in YYYY-MM-DD format.
    
    Args:
        date_str: The date string to parse
        
    Returns:
        datetime object if valid, None if invalid or empty
    """
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

def add_task(manager: TaskManager) -> None:
    """Handle adding a new task.
    
    Args:
        manager: The TaskManager instance to use
    """
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
    
    due_date = parse_date(due_date_str)
    if due_date_str and not due_date:
        print("Invalid date format. Task will be created without due date.")
    
    task = manager.add_task(title, description, due_date)
    print("\nTask created successfully!")
    print_task(task)

def list_tasks(manager: TaskManager) -> None:
    """Handle listing all tasks.
    
    Args:
        manager: The TaskManager instance to use
    """
    tasks = manager.list_tasks()
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTask List:")
        for task in tasks:
            print_task(task)

def mark_completed(manager: TaskManager) -> None:
    """Handle marking a task as completed.
    
    Args:
        manager: The TaskManager instance to use
    """
    task_id = input("Enter task ID to mark as completed: ")
    try:
        task_id = int(task_id)
        if manager.mark_completed(task_id):
            print("Task marked as completed!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid task ID.")

def delete_task(manager: TaskManager) -> None:
    """Handle deleting a task.
    
    Args:
        manager: The TaskManager instance to use
    """
    task_id = input("Enter task ID to delete: ")
    try:
        task_id = int(task_id)
        if manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid task ID.")

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
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_task(manager)
        elif choice == "2":
            list_tasks(manager)
        elif choice == "3":
            mark_completed(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 