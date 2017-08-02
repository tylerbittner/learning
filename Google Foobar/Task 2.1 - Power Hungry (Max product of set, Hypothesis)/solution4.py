# NOT TYLER'S CODE

def answer4(xs):
    '''
    returns max product of elements
    '''
    non_zeroes = {
        '+': [],
        '-': []
    }

    for e in xs:
        if e > 0:
            non_zeroes['+'].append(e)
        elif e < 0:
            non_zeroes['-'].append(e)
        # IGNORE INTEGER 0

    if len(non_zeroes['-']) % 2 == 1:  # CASE: odd no. of negatives
        non_zeroes['-'].remove(max(non_zeroes['-']))  # rm neg of smallest magnitude

    # ALL ELEMENTS IN XS == 0 / NO NON_ZERO ELEMENTS
    if non_zeroes['+'] == [] and non_zeroes['-'] == []:
        return '0'

    # FIND THE PRODUCT
    power = 1
    for _list in non_zeroes.values():
        for e in _list:
            power *= e

    return str(power)