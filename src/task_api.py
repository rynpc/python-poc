"""Provide API functions for task management operations."""

from datetime import datetime
from typing import List, Optional

from src.task_manager import Task, TaskManager


def add_task_api(
    manager: TaskManager, title: str, description: str, due_date: Optional[datetime]
) -> Task:
    """Add a task using the TaskManager API."""
    return manager.add_task(title, description, due_date)


def list_tasks_api(manager: TaskManager, include_completed: bool = False) -> List[Task]:
    """List tasks using the TaskManager API."""
    return manager.list_tasks(include_completed)


def mark_completed_api(manager: TaskManager, task_id: int) -> Task:
    """Mark a task as completed using the API."""
    return manager.mark_completed(task_id)


def delete_task_api(manager: TaskManager, task_id: int) -> None:
    """Delete a task using the API."""
    manager.delete_task(task_id)
