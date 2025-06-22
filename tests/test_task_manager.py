"""
Test module for TaskManager class.

This module contains unit tests for the TaskManager class, covering:
- Task creation (basic and with due date)
- Input validation for task creation
- Task retrieval by ID
- Task attribute updates
- Task deletion
- Task listing (all and incomplete only)
- Task completion status management

Each test focuses on a specific functionality to ensure the TaskManager
works as expected under various conditions.
"""

from datetime import datetime

import pytest

from src.task_manager import TaskManager


def test_add_task() -> None:
    """Test adding a basic task."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    assert task.id == 1
    assert task.title == "Test"
    assert task.description == "Test description"
    assert not task.completed
    assert task.due_date is None


def test_add_task_with_due_date() -> None:
    """Test adding a task with a due date."""
    manager = TaskManager()
    due_date = datetime(2024, 12, 31)
    task = manager.add_task("Test", "Test description", due_date)
    assert task.due_date == due_date


def test_add_task_validation() -> None:
    """Test validation when adding tasks."""
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("", "Description")
    with pytest.raises(ValueError):
        manager.add_task("Title", "")


def test_get_task() -> None:
    """Test retrieving a task by ID."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    retrieved = manager.get_task(task.id)
    assert retrieved == task


def test_get_nonexistent_task() -> None:
    """Test retrieving a non-existent task."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.get_task(1)


def test_update_task() -> None:
    """Test updating a task's attributes."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    due_date = datetime(2024, 12, 31)

    updated = manager.update_task(
        task.id, title="Updated", description="Updated description", due_date=due_date
    )

    assert updated.title == "Updated"
    assert updated.description == "Updated description"
    assert updated.due_date == due_date
    assert updated == task  # Should be the same object


def test_delete_task() -> None:
    """Test deleting a task."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    manager.delete_task(task.id)
    with pytest.raises(KeyError):
        manager.get_task(task.id)


def test_delete_nonexistent_task() -> None:
    """Test deleting a non-existent task."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.delete_task(1)


def test_list_tasks() -> None:
    """Test listing all tasks."""
    manager = TaskManager()
    task1 = manager.add_task("Test 1", "Description 1")
    task2 = manager.add_task("Test 2", "Description 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks


def test_list_incomplete_tasks() -> None:
    """Test listing only incomplete tasks."""
    manager = TaskManager()
    task1 = manager.add_task("Test 1", "Description 1")
    task2 = manager.add_task("Test 2", "Description 2")
    manager.mark_completed(task1.id)

    tasks = manager.list_tasks(include_completed=False)
    assert len(tasks) == 1
    assert task2 in tasks
    assert task1 not in tasks


def test_mark_completed() -> None:
    """Test marking a task as completed."""
    manager = TaskManager()
    task = manager.add_task("Test", "Test description")
    updated = manager.mark_completed(task.id)
    assert updated.completed
    assert task.completed  # Should update the original object

def test_add_and_get_task():
    m = TaskManager()
    t = m.add_task("Title", "Description", datetime(2025, 1, 1))
    assert t.title == "Title"
    assert t.description == "Description"
    assert isinstance(m.get_task(t.id), type(t))

def test_add_task_missing_fields():
    m = TaskManager()
    with pytest.raises(ValueError):
        m.add_task("", "desc")
    with pytest.raises(ValueError):
        m.add_task("title", "")

def test_update_task():
    m = TaskManager()
    t = m.add_task("T", "D")
    updated = m.update_task(t.id, title="T2", description="D2")
    assert updated.title == "T2"
    assert updated.description == "D2"

def test_update_task_invalid_id():
    m = TaskManager()
    with pytest.raises(KeyError):
        m.update_task(999, title="nope")

def test_delete_task():
    m = TaskManager()
    t = m.add_task("A", "B")
    m.delete_task(t.id)
    with pytest.raises(KeyError):
        m.get_task(t.id)

def test_list_tasks_and_mark_completed():
    m = TaskManager()
    t1 = m.add_task("A", "B")
    t2 = m.add_task("C", "D")
    m.mark_completed(t1.id)
    all_tasks = m.list_tasks()
    not_completed = m.list_tasks(include_completed=False)
    assert len(all_tasks) == 2
    assert len(not_completed) == 1
    assert not_completed[0].id == t2.id

def test_mark_completed_invalid_id():
    m = TaskManager()
    with pytest.raises(KeyError):
        m.mark_completed(123)

def test_get_task_invalid_id():
    m = TaskManager()
    with pytest.raises(KeyError):
        m.get_task(999)
