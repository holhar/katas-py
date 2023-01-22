import unittest

from katas.fundamentals.shortest_word import find_short

class TestShortestWord(unittest.TestCase):
    def test_find_short1(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

    def test_find_short2(self):
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)

    def test_find_short3(self):
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)

    def test_find_short4(self):
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)

    def test_find_short5(self):
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)  

    def test_find_short6(self):
        self.assertEqual(find_short("Let's travel abroad shall we"), 2)