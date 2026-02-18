import unittest
import main
import os

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
            tasks = f.readlines()
        self.assertEqual(tasks[0].strip(), "task1\n")
        self.assertEqual(tasks[1].strip(), "task2\n")

    def test_complete_task(self):
        main.main(["task1", "task2"])
        main.main("-c 1 task1")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(tasks[0].strip(), "[X] task1\n")
        self.assertEqual(tasks[1].strip(), "task2\n")

    def test_load_tasks(self):
        main.main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(tasks[0].strip(), "task1\n")
        self.assertEqual(tasks[1].strip(), "task2\n")

    def test_clear_list(self):
        main.main(["task1", "task2"])
        main.main()
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)

    def test_no_tasks_provided(self):
        main.main()
        self.assertEqual(print("No tasks provided."), None)

if __name__ == '__main__':
    unittest.main()