import unittest
# My code
from solution_rec import answer


class TestFuelInjectionPerfection(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(answer('1'), 0)
        self.assertEqual(answer('2'), 1)
        self.assertEqual(answer('3'), 2)
        self.assertEqual(answer('4'), 2)    # Provided case
        self.assertEqual(answer('5'), 3)
        self.assertEqual(answer('6'), 3)
        self.assertEqual(answer('7'), 4)
        self.assertEqual(answer('8'), 3)
        self.assertEqual(answer('9'), 4)
        self.assertEqual(answer('10'), 4)
        self.assertEqual(answer('11'), 5)
        self.assertEqual(answer('12'), 4)
        self.assertEqual(answer('13'), 5)
        self.assertEqual(answer('14'), 5)
        self.assertEqual(answer('15'), 5)      # Provided case
        self.assertEqual(answer('16'), 4)
        self.assertEqual(answer('17'), 5)

        self.assertEqual(answer('32'), 5)
        self.assertEqual(answer('64'), 6)
        self.assertEqual(answer('128'), 7)
        self.assertEqual(answer('256'), 8)
        self.assertEqual(answer('1024'), 10)

        # 34 digits
        self.assertEqual(answer('1234908145890798071230801278903589'), 147)
        # 100 digits
        self.assertEqual(answer('1234908145890798071230801278903589123490814589079807123080127890358912349081458907980712308012789035'), 434)
        # 200 digits
        self.assertEqual(answer('12349081458907980712308012789035891234908145890798071230801278903589123490814589079807123080127890351234908145890798071230801278903589123490814589079807123080127890358912349081458907980712308012789035'), 878)
        # 309 digits
        self.assertEqual(answer('123445698172306729487399879827412344569817230672948739987982741234456981723067294873998798274123445698172306729487399879827412344569817230672948739987982741234456981723067294873998798274123445698172306729487399879827412344569817230672948739987982741234456981723067294873998798274123445698172306729487399879821'), 1364)
        # 309 digits
        self.assertEqual(answer('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'), 1278)

        #self.assertEqual(answer(''), )


if __name__ == '__main__':
    unittest.main(verbosity=2)
