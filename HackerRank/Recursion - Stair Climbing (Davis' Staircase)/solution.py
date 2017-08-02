def climb_recursive(n, memo):
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # if n == 3:
    #     return 4

    # Alternative to above, from gaylemcd:
    # (This is simpler and uses the full power of recursion but I think the above is more understandable.)
    if n < 0:
        return 0
    if n == 0:
        return 1

    if n not in memo:
        memo[n] = climb_recursive(n - 1, memo) + climb_recursive(n - 2, memo) + climb_recursive(n - 3, memo)
    return memo[n]


# HackerRank's template code:
s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())

    # Tyler's code
    memo = {}
    print climb_recursive(n, memo)
