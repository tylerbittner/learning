import unittest

from hypothesis import given, assume
import hypothesis.strategies as st
import hypothesis.specifiers as sp

# My code
from solution import answer
from solution4 import answer4


class TestPowerHungry(unittest.TestCase):

    @given(st.lists(sp.integers_in_range(-1000, 1000)))
    def test_answer_hypothesis(self, xs):
        assume(xs)
        assume(len(xs) <= 50)
        print(xs)
        self.assertEqual(answer(xs), answer4(xs))


    def test_answer(self):
        # Example cases
        self.assertEqual(answer([2, -3, 1, 0, -5]), '30')
        self.assertEqual(answer([2, 0, 2, 2, 0]), '8')
        self.assertEqual(answer([-2, -3, 4, -5]), '60')
        # My cases
        self.assertEqual(answer([0, 0, -1]), '0')
        self.assertEqual(answer([0]), '0')
        self.assertEqual(answer([1]), '1')
        self.assertEqual(answer([-1]), '-1')
        self.assertEqual(answer([50]), '50')
        self.assertEqual(answer([-50]), '-50')
        self.assertEqual(answer([1000]), '1000')
        self.assertEqual(answer([-1000]), '-1000')
        self.assertEqual(answer([0, 0, 0]), '0')
        self.assertEqual(answer([1, 1, 1]), '1')
        self.assertEqual(answer([0, -5]), '0')
        self.assertEqual(answer([0, -5, -6]), '30')
        self.assertEqual(answer([0, -5, -6, -10]), '60')
        self.assertEqual(answer([-1, 7]), '7')
        self.assertEqual(answer([-1, -1, 7]), '7')
        self.assertEqual(answer([0, -1, 7]), '7')
        self.assertEqual(answer([0, 5]), '5')
        self.assertEqual(answer([-2, -2]), '4')
        self.assertEqual(answer([-2, -2, -2]), '4')
        self.assertEqual(answer([2, -2, 2]), '4')
        self.assertEqual(answer([-2, 2, -2]), '8')
        self.assertEqual(answer([-3, -2, 4, -5]), '60')
        self.assertEqual(answer([-3, 4, -5, -2]), '60')
        self.assertEqual(answer([-1, 1, -1, 1, -1, 1]), '1')
        self.assertEqual(answer([1000, 500, 1, 5]), '2500000')
        self.assertEqual(answer([1, 500, 1000, -5]), '500000')
        self.assertEqual(answer([-5, 1, 500, 1000]), '500000')
        self.assertEqual(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), '30414093201713378043612608166064768844377641568960512000000000000')
        self.assertEqual(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, -50]), '608281864034267560872252163321295376887552831379210240000000000')
        self.assertEqual(answer([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]), '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(answer(
            [-1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000,
             -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000,
             -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000]),
                         '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        #self.assertEqual(answer([]), )


if __name__ == '__main__':
    unittest.main(verbosity=2)
