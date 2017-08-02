def answer(chocolates, min_ops_cache):
    print 'DEBUG: chocolates =', chocolates

    # Base case: all interns have equal # of chocolates
    max_c = max(chocolates)
    min_c = min(chocolates)
    diff = max_c - min_c
    if diff == 0:
        return 0

    # Return cached values here
    if diff in min_ops_cache:
        return min_ops_cache[diff]

    # Operations to reduce to the base case
    min_ops_cache[diff] = diff
    for i in xrange(len(chocolates)):

        if chocolates[i] == min_c:
            continue

        # Give 1 to all others
        more_choc = list(chocolates)
        for j in xrange(len(more_choc)):
            if not j == i:
                more_choc[j] += 1
        ops = 1 + answer(more_choc, min_ops_cache)
        if ops < min_ops_cache[diff]:
            min_ops_cache[diff] = ops

        # Give 2 to all others
        more_choc = list(chocolates)
        for j in xrange(len(more_choc)):
            if not j == i:
                more_choc[j] += 2
        ops = 1 + answer(more_choc, min_ops_cache)
        if ops < min_ops_cache[diff]:
            min_ops_cache[diff] = ops

        # Give 5 to all others
        more_choc = list(chocolates)
        for j in xrange(len(more_choc)):
            if not j == i:
                more_choc[j] += 5
        ops = 1 + answer(more_choc, min_ops_cache)
        if ops < min_ops_cache[diff]:
            min_ops_cache[diff] = ops

    print 'DEBUG: min_ops_cache =', min_ops_cache
    return min_ops_cache[diff]


# Read input & call my code
num_testcases = int(raw_input().strip())
for i in xrange(num_testcases):
    n = int(raw_input().strip())
    n_chocolates = map(int, raw_input().strip().split(' '))
    print answer(n_chocolates, {})
