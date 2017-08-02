import unittest
# My code
from solution_v2_naive import answer


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
            lst[i] = (i + 1) * 499
        #print 'list[-1] =', lst[-1]        # 998000
        self.assertEqual(answer(lst), 40888)

    def test_answer_repeating_len_100(self):
        lst = [6] * 100
        self.assertEqual(answer(lst), 161700)

    # def test_answer_repeating_len_500(self):
    #     lst = [6] * 500
    #     self.assertEqual(answer(lst), 20708500)

    # Case: len(lst) <= 2
    def test_answer_bad1(self):
        self.assertEqual(answer([2, 4]), 0)



    # def test_answer_(self):
        # self.assertEqual(answer(), )


suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgo)
unittest.TextTestRunner(verbosity=2).run(suite)
