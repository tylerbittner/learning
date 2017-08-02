import heapq


def find_running_median(array):
    # NOTE: We store & compare *negatives* of items in the lower heap to force max heap behavior
    lower_max = []
    upper_min = []

    for item in array:
        if len(lower_max) == 0:
            heapq.heappush(lower_max, -item)
        else:
            # Try to add to upper heap or swap out of lower to maintain balance in length of each side
            if len(lower_max) > len(upper_min):
                if item >= abs(lower_max[0]):
                    heapq.heappush(upper_min, item)
                else:
                    swap_item = heapq.heapreplace(lower_max, -item)
                    heapq.heappush(upper_min, abs(swap_item))

            # Try to add to lower heap
            else:
                if item <= upper_min[0]:
                    heapq.heappush(lower_max, -item)
                else:
                    swap_item = heapq.heapreplace(upper_min, item)
                    heapq.heappush(lower_max, -swap_item)

        print_median(lower_max, upper_min)

    return


def print_median(lower_max, upper_min):

    median = 0
    full_n = len(lower_max) + len(upper_min)
    if full_n > 0 and full_n % 2 == 0:
        # length is even so average two middle numbers
        median = '%.1f' % ((abs(lower_max[0]) + upper_min[0]) / 2.0)
    else:
        median = '%.1f' % abs(lower_max[0])

    print median
    return


# Start HackerRank's Boilerplate
n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
# End HackerRank's Boilerplate

find_running_median(a)
