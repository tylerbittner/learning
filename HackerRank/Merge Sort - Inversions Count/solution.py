# Problem statement: https://www.hackerrank.com/challenges/ctci-merge-sort


def count_inversions(array):
    global inversions
    inversions = 0
    # Create temp array for merging only once for performance
    global temp_array
    temp_array = [0] * len(array)
    # Call recursive mergesort until we get two sorted arrays back
    mergesort_recursive(array, 0, len(array) - 1)
    return inversions


def mergesort_recursive(array, start, end):
    """Recursively sort an array"""

    # Check bounds to see if we're done
    if start >= end:
        return array
    middle = (start + end) / 2
    # Sort left half
    array = mergesort_recursive(array, start, middle)
    # Sort right half
    array = mergesort_recursive(array, middle + 1, end)
    # Merge two sorted halves & count inversions
    array = mergesort_count(array, start, end)

    return array


def mergesort_count(array, left_start, right_end):
    """Merge two sorted halves of given array & count inversions"""

    global inversions
    global temp_array

    # Get middle spots
    left_end = (left_start + right_end) / 2
    right_start = left_end + 1

    # Index to walk thru each array
    left_index = left_start
    right_index = right_start
    temp_index = left_start

    # Walk thru arrays comparing each item & putting smaller into temp array
    while (left_index <= left_end) and (right_index <= right_end):
        if array[left_index] <= array[right_index]:
            temp_array[temp_index] = array[left_index]
            left_index += 1
        else:
            temp_array[temp_index] = array[right_index]
            right_index += 1
            # Number of inversions done is the number of elements remaining in
            #   the left array when an element is copied from right array.
            # See Tom's Coursera lecture for explanation:
            #   "O(n log n) Algorithm for Counting Inversions II"
            inversions += left_end - left_index + 1
        temp_index += 1

    # Last step: once end of either array is reached, copy remainder onto end of
    # temp array slice then copy into original array slice
    temp_array[temp_index:temp_index + left_end - left_index + 1] = array[left_index:left_end + 1]
    temp_array[temp_index:temp_index + right_end - right_index + 1] = array[right_index:right_end + 1]
    array[left_start:right_end + 1] = temp_array[left_start:right_end + 1]

    return array


# HackerRank's template code:
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)
