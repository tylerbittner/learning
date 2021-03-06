#
# Commander Lambda # 3.3: Find the Access Codes
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#


def answer(lst):
    """Takes a list of positive integers l and counts the number of 'lucky triples' of 
    (lst[i], lst[j], lst[k]) where i < j < k."""

    if len(lst) <= 2:
        return 0

    num_triples = 0
    div_cache = {}

    cnt_used_cache = 0

    # i
    for i in xrange(len(lst) - 2):
        # print 'lst[i] = ', lst[i]
        # print 'div_cache: ', sorted(div_cache)

        # j
        for j in xrange(i + 1, len(lst) - 1):
            # print '---> lst[j] = ', lst[j]
            if (lst[i], lst[j]) in div_cache:
                # print '[Using cache for **lst[i], lst[j]** (', lst[i], lst[j], ')]'
                cnt_used_cache += 1
                if not div_cache[(lst[i], lst[j])] == 0:
                    continue
            elif not lst[j] % lst[i] == 0:
                continue

            # k
            for k in xrange(j + 1, len(lst)):
                # print '--------> lst[k] = ', lst[k]
                div_cache[(lst[j], lst[k])] = lst[k] % lst[j]
                #print 'Added to cache: (', lst[j], lst[k], ') = ', div_cache[(lst[j], lst[k])]
                if div_cache[(lst[j], lst[k])] == 0:
                    # print 'Lucky Triple found: ', lst[i], lst[j], lst[k]
                    num_triples += 1

    print 'cnt_used_cache =', cnt_used_cache
    print 'len(div_cache) =', len(div_cache)

    return num_triples


# For running with cProfile:
if __name__ == '__main__':
    main_lst = [0] * 2000
    for i in xrange(2000):
        main_lst[i] = (i + 1) * 499
    answer(main_lst)
