import unittest
import main
import os
import json

class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_todo.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_tasks(self):
        main.main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[1]["task"], "task2")

    def test_complete_task(self):
        main.main(["task1", "task2"])
        main.main("-c 1 task1")
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[0]["complete"], True)
        self.assertEqual(tasks[1]["task"], "task2")

    def test_load_tasks(self):
        main.main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[1]["task"], "task2")

    def test_clear_list(self):
        main.main(["task1", "task2"])
        main.main()
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 0)

    def test_no_tasks_provided(self):
        main.main()
        self.assertEqual(print("No tasks provided."), None)

    def test_complete_task_nonexistent(self):
        main.main(["task1", "task2"])
        main.main("-c 5 task1")
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[1]["task"], "task2")

    def test_complete_task_invalid_number(self):
        main.main(["task1", "task2"])
        main.main("-c abc task1")
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[1]["task"], "task2")

    def test_add_task_with_priority(self):
        main.main(["task1", "--priority High"])
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[0]["priority"], "High")

    def test_filter_by_priority(self):
        main.main(["task1", "task2", "--priority High"])
        with open("todo.txt", "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "task1")
        self.assertEqual(tasks[0]["priority"], "High")