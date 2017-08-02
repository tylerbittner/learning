# NOT TYLER'S CODE

import operator

def answer(xs):

    # Only a negative given
    if xs[0] < 0:
        return str(xs[0])

    legitVals = []
    negVals = []
    theSolution = 999
    if len(xs) == 1 and xs[0] == 0:
        theSolution = 0
    else:
        for index, value in enumerate(xs):
            if xs[index] > 0:
                legitVals.append(value)

            if xs[index] < 0:
                negVals.append(value)
    #print (legitVals)
    #print (negVals)
    #print (xs)
    negValsLength = len(negVals)
    legitValsLength = len(legitVals)
    if (legitValsLength > 0) and (negValsLength > 1):
        if negValsLength % 2 != 0:
            del negVals[negVals.index(max([n for n in xs if n < 0]))]
        theSolution = reduce(operator.mul, legitVals + negVals)
    elif negValsLength > 1:
        if negValsLength % 2 != 0:
            del negVals[negVals.index(max([n for n in xs if n < 0]))]
        theSolution = reduce(operator.mul, negVals)
    elif legitValsLength > 0:
        theSolution = reduce(operator.mul, legitVals)
    else:
        theSolution = 0
    return str(theSolution)
