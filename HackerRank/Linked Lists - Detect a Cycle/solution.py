"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    seen_nodes = {}
    seen_nodes[head] = True

    # Go thru linked list
    current_node = head
    while current_node:
        current_node = current_node.next
        if current_node in seen_nodes:
            return 1
        seen_nodes[current_node] = True

    return 0

