"""
Task Manager module for managing tasks in a simple task management system.

This module provides the core functionality for managing tasks, including:
- Adding new tasks with title, description, and optional due date
- Retrieving tasks by ID
- Updating existing tasks
- Deleting tasks
- Listing all tasks or filtering by completion status
- Marking tasks as completed

Example:
    >>> from task_manager import TaskManager, Task
    >>> manager = TaskManager()
    >>> task = manager.add_task("Write docs", "Document the codebase")
    >>> manager.mark_completed(task.id)
    >>> tasks = manager.list_tasks()
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Task:
    """
    A task in the task management system.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        due_date (Optional[datetime]): Optional due date for the task
        completed (bool): Whether the task is completed
    """

    id: int
    title: str
    description: str
    due_date: Optional[datetime] = None
    completed: bool = False


class TaskManager:
    """
    Manages tasks in the task management system.

    This class provides methods for creating, retrieving, updating,
    and deleting tasks, as well as listing tasks and marking them as completed.
    """

    def __init__(self) -> None:
        """Initialize an empty task manager."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(
        self, title: str, description: str, due_date: Optional[datetime] = None
    ) -> Task:
        """
        Add a new task to the manager.

        Args:
            title: The title of the task
            description: A detailed description of the task
            due_date: Optional due date for the task

        Returns:
            The newly created task

        Raises:
            ValueError: If title or description are empty
        """
        if not title or not description:
            raise ValueError("Title and description are required")

        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            due_date=due_date,
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The requested task

        Raises:
            KeyError: If the task ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        return self._tasks[task_id]

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
    ) -> Task:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            due_date: New due date (optional)

        Returns:
            The updated task

        Raises:
            KeyError: If the task ID doesn't exist
        """
        task = self.get_task(task_id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        return task

    def delete_task(self, task_id: int) -> None:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Raises:
            KeyError: If the task ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        del self._tasks[task_id]

    def list_tasks(self, include_completed: bool = True) -> List[Task]:
        """
        List all tasks, optionally filtering by completion status.

        Args:
            include_completed: Whether to include completed tasks

        Returns:
            A list of tasks matching the filter criteria
        """
        tasks = list(self._tasks.values())
        if not include_completed:
            tasks = [task for task in tasks if not task.completed]
        return tasks

    def mark_completed(self, task_id: int) -> Task:
        """
        Mark a task as completed.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            The updated task

        Raises:
            KeyError: If the task ID doesn't exist
        """
        task = self.get_task(task_id)
        task.completed = True
        return task
