#
# Commander Lambda # 3.1 - "Fuel Injection Perfection"
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#

from sys import setrecursionlimit


def answer(n):
    # Recursion limit of 1000 (the default in my env) is not enough to solve for a 309-digit number using this method -
    # looks like the largest valid n requires 4104 recursive calls.  So let's increase it to 5000.
    # Foobar's verify did not like a value of 10000, which works ok in my env.
    setrecursionlimit(5000)
    return answer_rec(int(n), {})


def answer_rec(n, min_ops_cache):
    """Recursive solution, memoized"""

    # Base case
    if n == 1:
        min_ops_cache[n] = 0
        return 0

    if n in min_ops_cache and min_ops_cache[n] > 0:
        return min_ops_cache[n]

    min_ops_cache[n] = n
    if n % 2 == 0:
        # Operation: divide by 2
        num_ops = 1 + answer_rec(n / 2, min_ops_cache)
        if num_ops < min_ops_cache[n]:
            min_ops_cache[n] = num_ops
    else:
        # Operation: subtract
        num_ops = 1 + answer_rec(n - 1, min_ops_cache)
        if num_ops < min_ops_cache[n]:
            min_ops_cache[n] = num_ops
        # Operation: add
        num_ops = 1 + answer_rec(n + 1, min_ops_cache)
        if num_ops < min_ops_cache[n]:
            min_ops_cache[n] = num_ops

    return min_ops_cache[n]
