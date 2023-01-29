import unittest

from katas.fundamentals.string_ends_with import ends_with

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

class TestEndsWith(unittest.TestCase):
    def test_ends_with_true_cases(self):
        for text, ending in fixed_tests_True:
            self.assertTrue(ends_with(text, ending))

    def test_ends_with_false_cases(self):
        for text, ending in fixed_tests_False:
            self.assertFalse(ends_with(text, ending))
