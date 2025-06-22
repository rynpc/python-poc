"""Unit tests for the task_api module."""

import unittest
from datetime import datetime

from src.task_api import (
    add_task_api,
    delete_task_api,
    list_tasks_api,
    mark_completed_api,
)
from src.task_manager import TaskManager


class TestTaskAPI(unittest.TestCase):
    """Test cases for the task API."""

    def setUp(self) -> None:
        """Set up a TaskManager instance for each test."""
        self.manager = TaskManager()

    def test_add_task(self) -> None:
        """Test adding a task via the API."""
        task = add_task_api(self.manager, "Title", "Desc", datetime(2025, 1, 1))
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.description, "Desc")
        self.assertEqual(task.due_date, datetime(2025, 1, 1))

    def test_list_tasks(self) -> None:
        """Test listing tasks via the API."""
        add_task_api(self.manager, "Test", "Desc", None)
        tasks = list_tasks_api(self.manager)
        self.assertEqual(len(tasks), 1)

    def test_mark_completed(self) -> None:
        """Test marking a task as completed via the API."""
        task = add_task_api(self.manager, "A", "B", None)
        marked = mark_completed_api(self.manager, task.id)
        self.assertTrue(marked.completed)

    def test_delete_task(self) -> None:
        """Test deleting a task via the API."""
        # Provide both a title and a non-empty description
        task = add_task_api(self.manager, "ToDelete", "This will be deleted", None)
        delete_task_api(self.manager, task.id)
        self.assertEqual(len(list_tasks_api(self.manager)), 0)


if __name__ == "__main__":
    unittest.main()
