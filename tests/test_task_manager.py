"""
Tests for the Task Manager module.

This module contains unit tests for the TaskManager class and its functionality,
including task creation, retrieval, updates, deletion, and listing.
"""

import pytest
from datetime import datetime
from src.task_manager import TaskManager, Task

@pytest.fixture
def task_manager():
    """Fixture that provides a fresh TaskManager instance for each test."""
    return TaskManager()

def test_add_task(task_manager):
    """Test adding a basic task."""
    task = task_manager.add_task("Test Task", "Test Description")
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.id == 1
    assert not task.completed

def test_add_task_with_due_date(task_manager):
    """Test adding a task with a due date."""
    due_date = datetime(2024, 12, 31)
    task = task_manager.add_task("Test Task", "Test Description", due_date)
    assert task.due_date == due_date

def test_add_task_validation(task_manager):
    """Test validation when adding tasks."""
    with pytest.raises(ValueError):
        task_manager.add_task("", "Description")
    with pytest.raises(ValueError):
        task_manager.add_task("Title", "")

def test_get_task(task_manager):
    """Test retrieving a task by ID."""
    task = task_manager.add_task("Test Task", "Test Description")
    retrieved_task = task_manager.get_task(task.id)
    assert retrieved_task == task

def test_get_nonexistent_task(task_manager):
    """Test retrieving a non-existent task."""
    assert task_manager.get_task(999) is None

def test_update_task(task_manager):
    """Test updating a task's attributes."""
    task = task_manager.add_task("Test Task", "Test Description")
    updated_task = task_manager.update_task(task.id, title="Updated Title")
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Test Description"

def test_delete_task(task_manager):
    """Test deleting a task."""
    task = task_manager.add_task("Test Task", "Test Description")
    assert task_manager.delete_task(task.id)
    assert task_manager.get_task(task.id) is None

def test_delete_nonexistent_task(task_manager):
    """Test deleting a non-existent task."""
    assert not task_manager.delete_task(999)

def test_list_tasks(task_manager):
    """Test listing all tasks."""
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks

def test_list_incomplete_tasks(task_manager):
    """Test listing only incomplete tasks."""
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task_manager.mark_completed(task1.id)

    incomplete_tasks = task_manager.list_tasks(show_completed=False)
    assert len(incomplete_tasks) == 1
    assert incomplete_tasks[0] == task2

def test_mark_completed(task_manager):
    """Test marking a task as completed."""
    task = task_manager.add_task("Test Task", "Test Description")
    assert not task.completed
    task_manager.mark_completed(task.id)
    assert task.completed 