import unittest
from unittest.mock import patch
from add_function import add_function

class TestsAdd(unittest.TestCase):
    def setUp(self):
        self.numbers = "1,2,3,1"
        self.numbers1 = "1;2;3;1"
        self.numbers2 = "1,2,3,-1"

    def test_add_receiving_string(self):
        expected_result = add_function(self.numbers, "")
        self.failureException(False, expected_result )

    def test_add_return_list(self):
        expected_result = add_function(self.numbers, "")
        self.assertIsInstance(expected_result, int)

    def test_sum_of_numbers(self):
        expected_result = add_function(self.numbers, "")
        self.assertEqual(7, expected_result)

    def test_specify_string(self):
        expected_result = add_function(self.numbers1, ";")
        self.assertEqual(7, expected_result)

    def test_dismiss_negatives(self):
        expected_result = add_function(self.numbers2, "")
        self.assertEqual(6, expected_result)