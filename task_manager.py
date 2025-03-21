from datetime import datetime
from typing import List, Optional, Dict
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: Optional[datetime] = None
    completed: bool = False

class TaskManager:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str, due_date: Optional[datetime] = None) -> Task:
        """Add a new task to the task manager."""
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
        """Retrieve a task by its ID."""
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, **kwargs) -> Optional[Task]:
        """Update an existing task."""
        task = self.tasks.get(task_id)
        if not task:
            return None
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """List all tasks, optionally filtering completed ones."""
        tasks = list(self.tasks.values())
        if not show_completed:
            tasks = [task for task in tasks if not task.completed]
        return tasks

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.tasks.get(task_id)
        if task:
            task.completed = True
            return True
        return False 