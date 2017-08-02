#
# Commander Lambda # 2.2: En Route Salute
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#


def answer(s):
    """Return total number of en route salutes in string!"""

    left_count = 0
    salute_count = 0

    for char in s:
        if char == '>':
            left_count += 1
        if char == '<':
            salute_count += left_count * 2

    return salute_count
