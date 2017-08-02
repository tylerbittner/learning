#
# Commander Lambda # 3.3: Find the Access Codes
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#
from collections import deque


def answer(l):
    """Takes a list of positive integers l and counts the number of 'lucky triples' of 
    (lst[i], lst[j], lst[k]) where i < j < k."""

    num_triples = 0
    meta_num_ops = 0

    # Store list values for quick access, with values of count of occurrences to handle many of same value
    d = dict([i, l.count(i)] for i in l)
    # Convert list to deque for quick access to front of list
    ld = deque(l)

    # Assumes list we're given is sorted ascending
    max_val = max(ld)

    while len(ld) > 2:
        x = ld.popleft()
        print 'x =', x
        # Decrease count for key or remove if zero
        # TODO: Make it a function?
        if d[x] > 1:
            d[x] -= 1
        else:
            del d[x]

        i = 1
        y_candidate = x * i
        if y_candidate <= max_val and y_candidate in d:
            y = y_candidate
            print '---> y =', y

            j = 1
            z_candidate = y * j
            if z_candidate <= max_val and z_candidate in d:
                # TODO: Please make this less ugly if possible
                if j == 1 and d[y] <= 1:
                    pass
                else:
                    print '*** Lucky Triple found: ', x, y, z_candidate, '***'
                    num_triples += 1

            j += 1

        i += 1

    return num_triples


# For running with cProfile:
if __name__ == '__main__':
    main_lst = [0] * 2000
    for i in xrange(2000):
        main_lst[i] = (i + 1) * 499
    answer(main_lst)
