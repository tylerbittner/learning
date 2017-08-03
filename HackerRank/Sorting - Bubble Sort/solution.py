# Problem statement: https://www.hackerrank.com/challenges/ctci-bubble-sort


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

total_swaps = 0
# We can skip the last element in each pass since it will be largest
unsorted_length = len(a) - 1

# Code from problem statement, ported to Python
for item in a:
    # Track number of elements swapped during a single array traversal
    swaps_this_pass = 0

    for i in xrange(0, unsorted_length):
        # Swap adjacent elements if they are in decreasing order
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaps_this_pass += 1
            total_swaps += 1

    unsorted_length -= 1

    # If no elements were swapped during a traversal, array is sorted
    if swaps_this_pass == 0:
        break

# Print results as specified
print 'Array is sorted in', total_swaps, 'swaps.'
print 'First Element:', a[0]
print 'Last Element:', a[-1]