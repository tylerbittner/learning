import unittest
# My code
from solution import answer


class TestAlgo(unittest.TestCase):

    def test_answer_provided1(self):
        self.assertEqual(answer([1, 1, 1]), 1)

    def test_answer_provided2(self):
        self.assertEqual(answer([1, 2, 3, 4, 5, 6]), 3)

    def test_answer_1(self):
        self.assertEqual(answer([2, 2, 2]), 1)

    def test_answer_2(self):
        self.assertEqual(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)

    def test_answer_3(self):
        self.assertEqual(answer([1, 2, 3, 3, 4, 5, 6]), 6)

    def test_answer_4(self):
        self.assertEqual(answer([1, 2, 3, 3, 3, 4, 5, 6]), 12)

    def test_answer_5(self):
        self.assertEqual(answer([1, 2, 3, 3, 3, 3, 4, 5, 6]), 22)

    def test_answer_len_30(self):
        lst = [0] * 30
        for i in xrange(30):
            lst[i] = i + 1
        self.assertEqual(answer(lst), 84)

    def test_answer_len_100(self):
        lst = [0] * 100
        for i in xrange(100):
            lst[i] = i + 1
        self.assertEqual(answer(lst), 607)

    def test_answer_len_2000(self):
        lst = [0] * 2000
        for i in xrange(2000):
            lst[i] = (i + 1) * 499      # Yields max of 998000
        self.assertEqual(answer(lst), 40888)
        # v2: meta_num_ops = 14509159
        # v4: meta_num_ops = 2105775
        # v4.1:            = 139844
        # v4.2:            = 155360
        # v5               = 2028034

    # START EXPERIMENT

    def test_answer_repeating_len_3(self):
        lst = [6] * 3
        self.assertEqual(answer(lst), 1)

    def test_answer_repeating_len_4(self):
        lst = [6] * 4
        self.assertEqual(answer(lst), 4)

    def test_answer_repeating_len_5(self):
        lst = [6] * 5
        self.assertEqual(answer(lst), 10)

    def test_answer_repeating_len_6(self):
        lst = [6] * 6
        self.assertEqual(answer(lst), 20)

    def test_answer_repeating_len_7(self):
        lst = [6] * 7
        self.assertEqual(answer(lst), 35)

    def test_answer_repeating_len_8(self):
        lst = [6] * 8
        self.assertEqual(answer(lst), 56)

    def test_answer_repeating_len_9(self):
        lst = [6] * 9
        self.assertEqual(answer(lst), 84)

    def test_answer_repeating_len_12(self):
        lst = [6] * 12
        self.assertEqual(answer(lst), 220)

    def test_answer_repeating_len_15(self):
        lst = [6] * 15
        self.assertEqual(answer(lst), 455)

    def test_answer_repeating_len_18(self):
        lst = [6] * 18
        self.assertEqual(answer(lst), 816)

    # END EXPERIMENT

    def test_answer_repeating_len_100(self):
        lst = [6] * 100
        self.assertEqual(answer(lst), 161700)

    def test_answer_repeating_len_500(self):
        lst = [6] * 500
        self.assertEqual(answer(lst), 20708500)

    def test_answer_repeating_len_2000(self):
        lst = [6] * 2000
        self.assertEqual(answer(lst), 1331334000)

    # Case: len(lst) <= 2
    def test_answer_bad1(self):
        self.assertEqual(answer([2, 4]), 0)

    # MAY NOT BE VALID CASE
    # Case: numbers do not follow i < j < k
    # def test_answer_bad2(self):
    #     self.assertEqual(answer([1, 4, 2]), 0)

    # def test_answer_(self):
        # self.assertEqual(answer(), )


suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgo)
unittest.TextTestRunner(verbosity=2).run(suite)
