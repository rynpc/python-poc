"""
Task Manager Module

This module provides a simple task management system with support for:
- Adding tasks with title, description, and optional due date
- Listing all tasks or only incomplete tasks
- Marking tasks as completed
- Deleting tasks
- Updating task details

Example:
    >>> manager = TaskManager()
    >>> task = manager.add_task("Buy groceries", "Milk, eggs, bread")
    >>> print(task.title)
    'Buy groceries'
"""

from datetime import datetime
from typing import List, Optional, Dict
from dataclasses import dataclass

@dataclass
class Task:
    """Represents a single task in the task manager.
    
    Attributes:
        id: Unique identifier for the task
        title: Task title
        description: Task description
        due_date: Optional due date for the task
        completed: Whether the task is completed
    """
    id: int
    title: str
    description: str
    due_date: Optional[datetime] = None
    completed: bool = False

class TaskManager:
    """Manages a collection of tasks with CRUD operations.
    
    This class provides methods to add, retrieve, update, and delete tasks,
    as well as list tasks and mark them as completed.
    """
    
    def __init__(self):
        """Initialize a new TaskManager with an empty task collection."""
        self.tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str, due_date: Optional[datetime] = None) -> Task:
        """Add a new task to the task manager.
        
        Args:
            title: The task title
            description: The task description
            due_date: Optional due date for the task
            
        Returns:
            The newly created Task object
            
        Raises:
            ValueError: If title or description is empty
        """
        if not title or not description:
            raise ValueError("Title and description are required")
        
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            due_date=due_date
        )
        self.tasks[task.id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, **kwargs) -> Optional[Task]:
        """Update an existing task's attributes.
        
        Args:
            task_id: The ID of the task to update
            **kwargs: Arbitrary keyword arguments for task attributes to update
            
        Returns:
            The updated Task object if found, None otherwise
        """
        task = self.tasks.get(task_id)
        if not task:
            return None
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if it wasn't found
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """List all tasks, optionally filtering completed ones.
        
        Args:
            show_completed: Whether to include completed tasks in the list
            
        Returns:
            List of Task objects
        """
        tasks = list(self.tasks.values())
        if not show_completed:
            tasks = [task for task in tasks if not task.completed]
        return tasks

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed.
        
        Args:
            task_id: The ID of the task to mark as completed
            
        Returns:
            True if the task was marked as completed, False if it wasn't found
        """
        task = self.tasks.get(task_id)
        if task:
            task.completed = True
            return True
        return False 