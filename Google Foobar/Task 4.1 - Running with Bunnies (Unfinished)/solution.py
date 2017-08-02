#
# Commander Lambda # 4.1: Running with Bunnies
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#

max_bunnies_grabbed = []

def answer(times, time_limit):
    """
    Calculates the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead
    before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of 
    bunnies with the lowest prisoner IDs (as indexes) in sorted order. 
    
    :param times: !!!
    :param time_limit: !!! 
    :return: List of bunnies picked up in the best solution sorted by prisoner ID.
    """

    n = len(times)
    start_row = 0
    end_row = n - 1

    global max_bunnies_grabbed

    bunnies_grabbed = backtrack(times, time_limit, 0, set())
    # Convert to "prisoner IDs"
    bunny_prisoner_ids = []
    if bunnies_grabbed:
        bunny_prisoner_ids = [i - 1 for i in sorted(bunnies_grabbed)]

    return bunny_prisoner_ids


def backtrack(times, time_left, row, bunnies_grabbed):
    """ Pseudocode for backtracking procedure
    
    In order to apply backtracking to a specific class of problems, one must provide the data P for the particular 
    instance of the problem that is to be solved, and six procedural parameters, root, reject, accept, first, next, 
    and output. These procedures should take the instance data P as a parameter and should do the following:

    1. root(P): return the partial candidate at the root of the search tree.
    2. reject(P,c): return true only if the partial candidate c is not worth completing.
    3. accept(P,c): return true if c is a solution of P, and false otherwise.
    4. first(P,c): generate the first extension of candidate c.
    5. next(P,s): generate the next alternative extension of a candidate, after the extension s.
    6. output(P,c): use the solution c of P, as appropriate to the application.
    
    The backtracking algorithm reduces the problem to the call bt(root(P)), where bt is the following recursive procedure:
    """

    global max_bunnies_grabbed

    if reject(times, time_left, row):
        return
    if accept(times, time_left, row):
        return output(times, time_left, row, bunnies_grabbed)

    next_row = get_next_candidate(times, time_left, row, bunnies_grabbed)

    while next_row:
        time_left -= times[row][next_row]

        backtrack(times, time_left, next_row, bunnies_grabbed)

        # TODO: I think this is wrong; instead try reconstructing the path (using prev vars) & use that to set grabbed
        add_grabbed_bunny(times, next_row, bunnies_grabbed)

        # Exit if we've found optimal solution
        if all_bunnies_grabbed(times):
            break

        next_row = get_next_candidate(times, time_left, next_row, bunnies_grabbed)

    return max_bunnies_grabbed


def reject(times, time_left, row):
    """
    Return true only if this CANDIDATE solution is NOT worth completing, false otherwise.
    
    Cases:
    1. time_left < 0 and no negative paths available from current row
    """
    # TODO: or if any negative paths, they cannot raise time_left to >= 0

    if time_left < 0 and not negative_paths_available(times, row):
        return True
    return False


def accept(times, time_left, row):
    """
    Returns true if we've reached a CANDIDATE solution, false otherwise.
    Cases:
    1. At bulkhead row, time_left >= 0, and no further paths available
    """
    if is_bulkhead(times, row):
        if all_bunnies_grabbed:
            return True
        if 0 <= time_left < max(times[row]) and not negative_paths_available(times, row):
            return True
    return False


def output(times, time_left, row, bunnies_grabbed):
    """
    ** REVIEW: Use the solution c of P, as appropriate to the application
    This is called for all success candidate solutions.
    """
    # TODO: Confirm whether updating max_bunnies_grabbed here makes sense
    global max_bunnies_grabbed
    if bunnies_grabbed and len(bunnies_grabbed) > len(max_bunnies_grabbed):
        max_bunnies_grabbed = bunnies_grabbed

    return


def get_next_candidate(times, time_left, start_row, bunnies_grabbed):
    """
    Generate the next candidate path.
    ** REVIEW: Must ensure every possible solution permutation occurs once and only once.
    """
    end_row = len(times) - 1

    # TODO: Return None to exit when all permutations have been exhausted... or the best guess anyway.

    unvisited_bunny_rows = [i for i in xrange(1, end_row) if not i == start_row]

    # Short-circuit to bulkhead if we know distance to it is greater than time limit
    for row in unvisited_bunny_rows:
        if bunnies_grabbed and row in bunnies_grabbed:
            unvisited_bunny_rows.remove(row)
        else:
            distance_to_end = times[start_row][row] + times[start_row][end_row]
            if distance_to_end > time_left:
                unvisited_bunny_rows.remove(row)

    # TODO: if there are negative paths greater than time_left, return them as options

    result = unvisited_bunny_rows[0] if unvisited_bunny_rows else end_row
    return result


def add_grabbed_bunny(times, row, bunnies_grabbed):
    """
    Add row to list of bunnies grabbed if it's a bunny row.
    """
    if row in xrange(1, len(times) - 1):
        bunnies_grabbed.add(row)
    return


def is_bulkhead(times, row):
    return row == len(times) - 1


def negative_paths_available(times, row):
    """
    Returns rows which have negative-weighted paths from here. 
    """
    neg_paths = [i for i, j in enumerate(times[row]) if j < 0]
    return neg_paths


def all_bunnies_grabbed(times):
    global max_bunnies_grabbed
    if len(max_bunnies_grabbed) == len(times) - 2:
        return True
    else:
        return False


# For calling with cProfile
# if __name__ == '__main__':
#     times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#     time_limit = 1
#     answer(times, time_limit)
