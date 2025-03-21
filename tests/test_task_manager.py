"""
Test module for TaskManager class.

Tests all functionalities including:
- Task creation and validation
- Task retrieval and updates
- Task deletion
- Task listing and filtering
- Task completion marking
"""

import pytest
from datetime import datetime
from src.task_manager import TaskManager, Task

def test_add_task():
    """Test adding a basic task."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    assert task.id == 1
    assert task.title == "Test"
    assert task.description == "Test description"
    assert not task.completed
    assert task.due_date is None

def test_add_task_with_due_date():
    """Test adding a task with a due date."""
    manager = TaskManager()
    due_date = datetime(2024, 12, 31)
    task = manager.add_task("Test", "Test description", due_date)
    assert task.due_date == due_date

def test_add_task_validation():
    """Test validation when adding tasks."""
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("", "Description")
    with pytest.raises(ValueError):
        manager.add_task("Title", "")

def test_get_task():
    """Test retrieving a task by ID."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    retrieved = manager.get_task(task.id)
    assert retrieved == task

def test_get_nonexistent_task():
    """Test retrieving a non-existent task."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.get_task(1)

def test_update_task():
    """Test updating a task's attributes."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    due_date = datetime(2024, 12, 31)
    
    updated = manager.update_task(
        task.id,
        title="Updated",
        description="Updated description",
        due_date=due_date
    )
    
    assert updated.title == "Updated"
    assert updated.description == "Updated description"
    assert updated.due_date == due_date
    assert updated == task  # Should be the same object

def test_delete_task():
    """Test deleting a task."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    manager.delete_task(task.id)
    with pytest.raises(KeyError):
        manager.get_task(task.id)

def test_delete_nonexistent_task():
    """Test deleting a non-existent task."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.delete_task(1)

def test_list_tasks():
    """Test listing all tasks."""
    manager = TaskManager()
    task1 = manager.add_task("Test 1", "Description 1")
    task2 = manager.add_task("Test 2", "Description 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks

def test_list_incomplete_tasks():
    """Test listing only incomplete tasks."""
    manager = TaskManager()
    task1 = manager.add_task("Test 1", "Description 1")
    task2 = manager.add_task("Test 2", "Description 2")
    manager.mark_completed(task1.id)
    
    tasks = manager.list_tasks(include_completed=False)
    assert len(tasks) == 1
    assert task2 in tasks
    assert task1 not in tasks

def test_mark_completed():
    """Test marking a task as completed."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    updated = manager.mark_completed(task.id)
    assert updated.completed
    assert task.completed  # Should update the original object 