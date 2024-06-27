import unittest
from task import Task

class test_task(unittest.TestCase):
    def setUp(self):
        """Test for Task object"""
        self.task = Task("d", "get plates", 1000)

    def test_initial_state(self):
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.task, "get plates")
        self.assertEqual(self.task.status, "d")
        self.assertEqual(self.task.priority, 1000)

if __name__ == "__main__":
    unittest.main()