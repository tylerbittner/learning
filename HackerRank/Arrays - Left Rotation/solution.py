def array_left_rotation(a, n, k):
    # a - array of integers to rotate
    # n - the number of integers in array
    # k - the number of left rotations to perform

    for i in xrange(k):
        x = a[0]
        del a[0]
        a.append(x)

    return a


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))

