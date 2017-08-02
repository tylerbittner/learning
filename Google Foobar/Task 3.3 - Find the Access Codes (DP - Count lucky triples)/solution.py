#
# Commander Lambda # 3.3: Find the Access Codes
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#


def answer(lst):
    """Takes a list of positive integers and counts the number of 'lucky triples' of (lst[i], lst[j], lst[k]) 
    where i < j < k.
    This solution is based on the fact that if an integer is both a divisor (the number being divided by) and a
    dividend (the number being divided) it's in the middle of a lucky triple.
    Solution is O(n**2) time complexity. """

    # Count number of divisors and dividends (the subproblems)
    divisor_for_cnt = [0] * len(lst)
    dividend_for_cnt = [0] * len(lst)
    for i in xrange(len(lst) - 1):
        for j in xrange(i + 1, len(lst)):
            if lst[j] % lst[i] == 0:
                divisor_for_cnt[i] += 1
                dividend_for_cnt[j] += 1

    # Combine results of subproblems
    lucky_triples_cnt = 0
    for k in xrange(1, len(lst) - 1):
        lucky_triples_cnt += divisor_for_cnt[k] * dividend_for_cnt[k]

    return lucky_triples_cnt
