import unittest
import os
from task1.task_1 import Open
class TestOpen(unittest.TestCase):
    def test_is_opened_file(self):
        with Open("test.txt","w") as f:
            self.assertFalse(f.closed)
            f.close()
    def test_file_exist(self):
        with Open("test.txt","w") as f:
            self.assertTrue(os.path.exists("test.txt"))
    def test_logger_file_exist(self):
        self.assertTrue(os.path.exists("logger.txt"))
    def test_open_counter(self):
        with Open("some_test.txt","r") as f:
            f.close()
        with Open("some_test.txt","r") as f:
            f.close()
        self.assertEqual(Open.get_counter(),2)
