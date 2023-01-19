import unittest

from katas.math.sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        """
        Test that it can sum a list of integers
        """
        result = sum(3, 3)
        self.assertEqual(result, 6)