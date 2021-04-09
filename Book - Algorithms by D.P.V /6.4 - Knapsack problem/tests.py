import unittest
# My code
from solution import answer_unlimited, answer_limited


class TestAlgo(unittest.TestCase):

    def test_answer_unlimited_provided1(self):
        # Total bag weight = 10
        # Item  Weight  Value
        # 1     6       $30
        # 2     3       $14
        # 3     4       $16
        # 4     2       $9
        self.assertEqual(answer_unlimited(10, [[6, 30], [3, 14], [4, 16], [2, 9]]), 48)

    def test_answer_limited_provided1(self):
        # Total bag weight = 10
        # Item  Weight  Value
        # 1     6       $30
        # 2     3       $14
        # 3     4       $16
        # 4     2       $9
        self.assertEqual(answer_limited(10, [[6, 30], [3, 14], [4, 16], [2, 9]]), 46)
