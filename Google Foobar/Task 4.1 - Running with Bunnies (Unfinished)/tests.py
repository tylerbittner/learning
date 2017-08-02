import unittest
import sys
# My code
from solution import answer


class TestAlgo(unittest.TestCase):

    def test_answer_provided1(self):
        """
        This case is undirected/symmetrical with no negative weights or negative-weighted cycles, and CANNOT be solved
        within the time limit.
        So the standard TSP should work with the addition of handling the time-limit bound.
        """
        times = [
            [0, 1, 1, 1, 1],    # 0 = Start
            [1, 0, 1, 1, 1],    # 1 = Bunny 0
            [1, 1, 0, 1, 1],    # 2 = Bunny 1
            [1, 1, 1, 0, 1],    # 3 = Bunny 2
            [1, 1, 1, 1, 0]     # 4 = Bulkhead
        ]
        time_limit = 3
        self.assertEqual(answer(times, time_limit), [0, 1])

    @unittest.skip("Not implemented yet")
    def test_answer_provided2(self):
        """
        This case is directed/asymmetrical with negative weights and negative-weighted cycles (I think), and cannot 
        rescue all bunnies within time limit.
        """
        times = [
            [0, 2, 2, 2, -1],  # 0 = Start
            [9, 0, 2, 2, -1],  # 1 = Bunny 0
            [9, 3, 0, 2, -1],  # 2 = Bunny 1
            [9, 3, 2, 0, -1],  # 3 = Bunny 2
            [9, 3, 2, 2,  0],  # 4 = Bulkhead
        ]
        time_limit = 1
        self.assertEqual(answer(times, time_limit), [1, 2])

    @unittest.skip("Not implemented yet")
    def test_answer_1(self):
        """ 
        Simple symmetrical paths, no time limit
        """
        times = [
            [0, 10, 5, 1, 1],  # 0 = Start
            [10, 0, 3, 1, 1],  # 1 = Bunny 0
            [5,  3, 0, 2, 1],  # 2 = Bunny 1
            [1,  1, 2, 0, 1],  # 3 = Bunny 2
            [1,  1, 1, 1, 0]   # 4 = Bulkhead
        ]
        # Sequential path distance = 10 + 3 + 2 + 1 = 16
        # Best path: 0, 3, 1, 2, 4; distance = 1 + 1 + 3 + 1 = 6
        time_limit = sys.maxint
        self.assertEqual(answer(times, time_limit), [0, 1, 2])

    @unittest.skip("Passed")
    def test_answer_2(self):
        """ 
        This case is undirected/symmetrical with no negative weights or negative-weighted cycles, and all bunnies
        can be rescued within the time limit.
        So the standard TSP should work -- except we end at bulkhead node, not back at the start.
        """
        times = [
            [0, 1, 1, 1, 1],  # 0 = Start
            [1, 0, 1, 1, 1],  # 1 = Bunny 0
            [1, 1, 0, 1, 1],  # 2 = Bunny 1
            [1, 1, 1, 0, 1],  # 3 = Bunny 2
            [1, 1, 1, 1, 0]   # 4 = Bulkhead
        ]
        # Sequential path distance = 1 + 1 + 1 + 1 = 4
        # Best path: 0, 1, 2, 3, 4; distance = 4
        time_limit = sys.maxint
        self.assertEqual(answer(times, time_limit), [0, 1, 2])

    @unittest.skip("Not impl yet")
    def test_answer_max_dim_matrix(self):
        times = [
            [0, 1, 1, 1, 1, 1, 1],  # 0 = Start
            [1, 0, 1, 1, 1, 1, 1],  # 1 = Bunny 0
            [1, 1, 0, 1, 1, 1, 1],  # 2 = Bunny 1
            [1, 1, 1, 0, 1, 1, 1],  # 3 = Bunny 2
            [1, 1, 1, 1, 0, 1, 1],  # 4 = Bunny 3
            [1, 1, 1, 1, 1, 0, 1],  # 5 = Bunny 4
            [1, 1, 1, 1, 1, 1, 0]   # 6 = Bulkhead
        ]
        # Sequential path distance = 1 + 1 + 1 + 1 = 6
        # Best path: 0, 1, 2, 3, 4, 5, 6; distance = 6
        time_limit = sys.maxint
        self.assertEqual(answer(times, time_limit), [0, 1, 2, 3, 4])

    @unittest.skip("Passed")
    def test_answer_neg_weights(self):
        times = [
            [0, 1, 1, 1, 1],  # 0 = Start
            [1, 0, 1, 1, 1],  # 1 = Bunny 0
            [1, 1, 0, 1, -1],  # 2 = Bunny 1
            [1, 1, 1, 0, 1],  # 3 = Bunny 2
            [1, 1, 1, 1, 0]   # 4 = Bulkhead
        ]
        time_limit = 2
        self.assertEqual(answer(times, time_limit), [0, 1])

    @unittest.skip("In-progress")
    def test_answer_with_cycles(self):
        times = [
            [0, 2, 2, 2, -1],  # 0 = Start
            [2, 0, 2, 2, -1],  # 1 = Bunny 0
            [2, 2, 0, 2, -1],  # 2 = Bunny 1
            [2, 2, 2, 0, -1],  # 3 = Bunny 2
            [2, 2, 2, 2, 0],  # 4 = Bulkhead
        ]
        # Sequential path distance = ??? = ???
        # Best path: ???; distance = 6
        time_limit = 1
        self.assertEqual(answer(times, time_limit), [0])

    # Cases to cover:
    # - A path with higher cost leads to grabbing MORE BUNNIES than another path
    # - There are at most 5 bunnies (which means 7 nodes total)
    # - time_limit is a non-negative integer that is at most 999
    # If "verify" test cases fail:
    # - Negative distance path is to row(s) other than bulkhead
    # - Multiple different values of negative distances
    # - Case where a negative cycle must be followed like 999 times to get under time limit
    # - In permutations-based approach, the shortest path to next node in set is indirect (so use a SP algo for this
    #   step in the process; altho we could possibly run into a cycle in the process)
    # - Paths with zero weight.  To get to bulkhead for example.

    # def test_answer_(self):
        # self.assertEqual(answer(''), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
