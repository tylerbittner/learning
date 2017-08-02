#
# Commander Lambda # 4.1: Running with Bunnies
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#
import sys
from itertools import combinations


def answer(times, time_limit):
    """
    Calculates the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead
    before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of 
    bunnies with the lowest prisoner IDs (as indexes) in sorted order. 
    
    :param times: !!!
    :param time_limit: !!! 
    :return: List of bunnies picked up in the best solution sorted by prisoner ID.
    """

    bunnies_grabbed = []

    n = len(times)
    C_shortest_paths = {(0,): [0] * n}
    # Redundant: C_shortest_paths[(0)][0] = 0

    for set_size in xrange(1, n):
        for subset in combinations(xrange(1, n), set_size):    # subset must contain 0
            subset_incl_start = tuple([0] + list(subset))
            C_shortest_paths[subset_incl_start] = [sys.maxint] * n
            for j in subset_incl_start:

                # ?? exclude zero which we just included??
                # maybe cause i still includes zero; we have to iter thru i too.
                if j == 0:
                    continue
                subset_ex_j = subset != j
                print

                #shortest_candidate =


    return 1

# For calling with cProfile
# if __name__ == '__main__':
#     times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#     time_limit = 1
#     answer(times, time_limit)
