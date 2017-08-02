from math import sqrt, floor


def primality_test(n):
    # Handle special cases
    if n == 2:
        print 'Prime'
        return
    # 1 and even numbers are not prime
    if n == 1 or int(str(n)[-1:]) in [2, 4, 6, 8, 0]:
        print 'Not prime'
        return
    # See https://en.wikipedia.org/wiki/Primality_test#Simple_methods
    # for why we only need to test up to the sqrt of n.  Cool intuition.
    max_to_test = int(floor(sqrt(n))) + 1
    for i in xrange(3, max_to_test, 2):
        if n % i == 0:
            print 'Not prime'
            return

    print 'Prime'
    return


# HackerRank's template code
p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    # Tyler's Code
    primality_test(n)
