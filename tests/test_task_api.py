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
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = add_task_api(self.manager, "Title", "Desc", datetime(2025, 1, 1))
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.description, "Desc")
        self.assertEqual(task.due_date, datetime(2025, 1, 1))

    def test_list_tasks(self):
        add_task_api(self.manager, "Test", "Desc", None)
        tasks = list_tasks_api(self.manager)
        self.assertEqual(len(tasks), 1)

    def test_mark_completed(self):
        task = add_task_api(self.manager, "A", "B", None)
        marked = mark_completed_api(self.manager, task.id)
        self.assertTrue(marked.completed)

    def test_delete_task(self):
        task = add_task_api(self.manager, "ToDelete", "", None)
        delete_task_api(self.manager, task.id)
        self.assertEqual(len(list_tasks_api(self.manager)), 0)


if __name__ == "__main__":
    unittest.main()
