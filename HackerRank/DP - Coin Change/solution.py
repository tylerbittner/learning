# Problem statement: https://www.hackerrank.com/challenges/ctci-coin-change


def make_change(coins, n):
    """Iterative solution"""
    if n < 0:
        return 0
    if n == 0:
        return 1
    solutions = [0] * (n + 1)
    solutions[0] = 1
    for coin in coins:
        total = coin
        while total <= n:
            solutions[total] += solutions[total - coin]
            total += 1
    return solutions[n]


# def make_change(coins, n):
#     """Recursive solution"""
#     global last_coin_used
#
#     if n < 0:
#         return 0
#     if n == 0:
#         # Found a solution set. Reset tracking.
#         last_coin_used = 0
#         print '.'
#         return 1
#
#     print '(n:', n, ')',
#
#     for c in sorted(coins):  # TODO: iter with value and index here
#         if i > 0 and last_coin_used == 0:
#             last_coin_used = coins[i - 1]
#         if c >= last_coin_used:
#             print 'coin:', c,
#             result += make_change(coins, n - c)
#
#     print
#     return result


# HackerRank's code
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))

# Tyler's changes
# To track which coin has already been tried between recursive calls
# global last_coin_used
# last_coin_used = 0

print make_change(coins, n)
