def ice_cream_parlor(m, a):
    '''Does given challenge'''

    cost_d = {}
    # Loop thru array putting in a dict
    for i, cost in enumerate(a):
        # while here check to see if cost + dict[remainder] == m has been seen yet
        needed_cost = m - cost

        # NOTE: According to teh HR editorial a binary search is used here to to find the matching cost instead of
        # a hashmap.  In order to use binary search an object or map of costs w/ IDs would need to be sorted first.

        if needed_cost in cost_d:
            # Matching cost found
            print cost_d[needed_cost] + 1, i + 1
            break

        # Not found, so put in dict & move on
        cost_d[cost] = i


# HackerRank's code
t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))

    # Call my code
    ice_cream_parlor(m, a)