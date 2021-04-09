import numpy as np


def answer_unlimited(W, items):
    """
    Solve knapsack problem variety where we can choose an unlimited number of each item.
    Implemented as explained in Chapter 6 of Algorithms by D.P.V.
    
    :param W: Total weight of knapsack 
    :param items: List of items to choose from as tuples of (weight, value)
    :return: Max value that can be fit
    """
    K_max_values = [0] * (W + 1)
    for w in range(1, W + 1):
        for (item_weight, item_value) in items:
            if item_weight <= w:
                candidate_value = K_max_values[w - item_weight] + item_value    # <-- KEY LINE OF SUBPROBLEM
                if candidate_value > K_max_values[w]:
                    K_max_values[w] = candidate_value
        # print 'K_max_values =', K_max_values

    return K_max_values[W]


def answer_limited(W, items):
    """
    Solve knapsack problem variety where we can only pick one of each item.
    Implemented as explained in Chapter 6 of Algorithms by D.P.V.
    
    :param W: Total weight of knapsack 
    :param items: List of items to choose from as tuples of (weight, value)
    :return: Max value that can be fit
    """

    # Init W x j 2D array
    #  Base case is 0 items, 0 weight bag
    n = len(items)
    K_max_values = np.matrix([[0] * (n + 1)] * (W + 1))
    print('K_max_values =\n', K_max_values)

    for j in range(1, n + 1):
        for w in range(1, W + 1):
            # Note the indexing used for the items list is 1 off from j since it's zero-based
            item_weight, item_value = items[j - 1]
            if item_weight > w:
                K_max_values[w, j] = K_max_values[w, j - 1]
            else:
                value_with_item = K_max_values[w - item_weight, j - 1] + item_value  # <-- KEY LINE OF SUBPROBLEM
                value_without_item = K_max_values[w, j - 1]
                if value_with_item > value_without_item:
                    K_max_values[w, j] = value_with_item
                else:
                    K_max_values[w, j] = value_without_item
        # print 'K_max_values =\n', K_max_values

    return K_max_values[W, n]
