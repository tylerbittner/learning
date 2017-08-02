#
# Commander Lambda # 2.1: Power Hungry
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#


def answer(xs):
    """Returns maximum possible product of a set of non-empty integers given in array"""

    # Special case: only a negative given
    if len(xs) == 1 and xs[0] < 0:
        return str(xs[0])

    positives = []
    negatives = []
    for num in xs:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)

    # Remove smallest abs value from negatives if odd length to get positive result.
    if len(negatives) % 2 > 0:
        negatives.remove(max(negatives))

    # Special case: array must be all zeros
    if len(positives) == 0 and len(negatives) == 0:
        return '0'

    max_product = 1
    for num in positives:
        max_product *= num
    for neg_num in negatives:
        max_product *= neg_num

    return str(max_product)
