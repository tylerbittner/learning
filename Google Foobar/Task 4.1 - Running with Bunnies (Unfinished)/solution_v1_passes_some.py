#
# Commander Lambda # 4.1: Running with Bunnies
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#
import sys
from itertools import permutations


def answer(times, time_limit):
    """
    Calculates the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead
    before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of 
    bunnies with the lowest prisoner IDs (as indexes) in sorted order. 
    
    :param times: !!!
    :param time_limit: !!! 
    :return: List of bunnies picked up in the best solution sorted by prisoner ID.
    """

    """
    Naive Solution: (from http://www.geeksforgeeks.org/travelling-salesman-problem-set-1/)
    1) Consider city 1 as the starting and ending point.
    2) Generate all (n-1)! Permutations of cities.
    3) Calculate cost of every permutation and keep track of minimum cost permutation.
    4) Return the permutation with minimum cost.
    """

    n = len(times)
    start_row = 0
    end_row = n - 1

    max_bunnies_grabbed = []
    min_distance = sys.maxint
    for perm in permutations(xrange(1, n - 1)):
        # print perm
        # Sum the distances from start thru permutations to end
        prev_row = start_row
        distance = 0
        distance_to_end = 0
        bunnies_grabbed = []
        for row in perm:
            # print 'Adding distance:', times[prev_index][i]
            distance += times[prev_row][row]
            prev_row = row

            # Short-circuit to bulkhead if we know distance to it is greater than time limit
            distance_to_end = times[row][end_row]
            if distance + distance_to_end > time_limit:
                break

            bunnies_grabbed.append(row - 1)

        # print 'Adding last hop:', times[perm[-1]][end]
        distance += distance_to_end
        # print '*** distance for this perm:', distance
        print 'bunnies_grabbed =', max_bunnies_grabbed

        if distance < min_distance:
            min_distance = distance
        if len(bunnies_grabbed) > len(max_bunnies_grabbed):
            max_bunnies_grabbed = bunnies_grabbed

    print 'min_distance =', min_distance
    return max_bunnies_grabbed


# For calling with cProfile
# if __name__ == '__main__':
#     times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#     time_limit = 1
#     answer(times, time_limit)
