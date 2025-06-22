from datetime import datetime
from typing import Optional

from src.task_api import (
    add_task_api,
    delete_task_api,
    list_tasks_api,
    mark_completed_api,
)
from src.task_manager import Task, TaskManager


def print_task(task: Task) -> None:
    status = "✓" if task.completed else " "
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
    print(f"\n[{status}] Task {task.id}: {task.title}")
    print(f"Description: {task.description}")
    print(f"Due date: {due_date}")


def parse_date(date_str: str) -> Optional[datetime]:
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return None


def add_task_cli(manager: TaskManager) -> None:
    print("\nAdd a new task:")
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    date_str = input("Due date (YYYY-MM-DD, or press Enter to skip): ").strip()
    due_date = parse_date(date_str)
    if due_date is None and date_str:
        return
    try:
        task = add_task_api(manager, title, description, due_date)
        print("\nTask added successfully!")
        print_task(task)
    except ValueError as e:
        print(f"\nError: {e}")


def list_tasks_cli(manager: TaskManager) -> None:
    include_completed = input("\nInclude completed tasks? (y/N): ").lower() == "y"
    tasks = list_tasks_api(manager, include_completed)
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nTasks:")
    for task in tasks:
        print_task(task)


def mark_completed_cli(manager: TaskManager) -> None:
    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))
        task = mark_completed_api(manager, task_id)
        print("\nTask marked as completed:")
        print_task(task)
    except ValueError:
        print("\nError: Invalid task ID")
    except KeyError as e:
        print(f"\nError: {e}")


def delete_task_cli(manager: TaskManager) -> None:
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        delete_task_api(manager, task_id)
        print("\nTask deleted successfully!")
    except ValueError:
        print("\nError: Invalid task ID")
    except KeyError as e:
        print(f"\nError: {e}")


def print_menu() -> None:
    print("\nTask Manager Menu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main() -> None:
    manager = TaskManager()
    actions = {
        "1": add_task_cli,
        "2": list_tasks_cli,
        "3": mark_completed_cli,
        "4": delete_task_cli,
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
