import unittest
from unittest.mock import patch
from add_function import add_function

class TestsAdd(unittest.TestCase):
    def setUp(self):
        self.numbers = "1,2,3,1"

    def test_add_receiving_string(self):
        expected_result = add_function(self.numbers)
        self.failureException(False, expected_result )

    def test_add_return_list(self):
        expected_result = add_function(self.numbers)
        self.assertEqual([], expected_result)

