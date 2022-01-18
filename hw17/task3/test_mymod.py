import unittest
from task3.mymod import test


class MyModTest(unittest.TestCase):
    def setUp(self):
        self.test = test

    def test_result(self):
        self.assertEqual(self.test("text.txt"), "2 lines, 12 chars")
