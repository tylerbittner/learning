# Problem statement: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import inspect


def check_binary_search_tree_(root):
    '''Validates this is really a binary tree such that:
        1. node.left.data < node.data < node.right.data.
        2. current data value > last data value (assumes in-order traversal)
        3. no nodes are equal (implicit thru < and > comparisons)'''

    node = root
    last = None

    if validate_tree(node, last):
        return True

    return False


def validate_tree(node, last):

    # Check left nodes
    if node.left:
        if not node.left.data < node.data:
            # print 'INVALID BST: not node.left.data (', node.left.data, ') < node.data (', node.data, ')'
            return False
        last = validate_tree(node.left, last)
        if not last:
            return False

    # *** NOTE: This location in the logic is KEY to in-order traversal. It's where the magic happens.

    if last:
        if not node.data > last.data:
            # print 'INVALID BST: not node.data (', node.data, ') > last.data (', last.data, ')'
            return False

    # print 'Setting new last value here to ', node.data
    last = node

    # Check right nodes
    if node.right:
        if not node.right.data > node.data:
            # print 'INVALID BST: not node.right.data (', node.right.data, ') > node.data (', node.data, ')'
            return False
        last = validate_tree(node.right, last)
        if not last:
            return False

    return last
