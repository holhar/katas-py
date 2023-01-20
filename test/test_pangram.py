import unittest

from katas.fundamentals.pandram import is_pangram

class TestPangram(unittest.TestCase):
    def test_pangram(self):        
        self.assertEqual(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)

    def test_not_pangram(self):        
        self.assertEqual(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)