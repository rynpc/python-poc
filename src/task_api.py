from datetime import datetime
from typing import Optional, List
from src.task_manager import Task, TaskManager

def add_task_api(manager: TaskManager, title: str, description: str, due_date: Optional[datetime]) -> Task:
    return manager.add_task(title, description, due_date)

def list_tasks_api(manager: TaskManager, include_completed: bool = False) -> List[Task]:
    return manager.list_tasks(include_completed)

def mark_completed_api(manager: TaskManager, task_id: int) -> Task:
    return manager.mark_completed(task_id)

def delete_task_api(manager: TaskManager, task_id: int) -> None:
    manager.delete_task(task_id)
