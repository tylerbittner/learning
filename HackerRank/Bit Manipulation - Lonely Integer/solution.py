def lonely_integer(a):
    result = 0
    for number in a:
        result ^= number
    return result

# HackerRank's template code
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
print lonely_integer(a)