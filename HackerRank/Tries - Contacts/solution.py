# Problem statement: https://www.hackerrank.com/challenges/ctci-contacts


# import pprint

# Use a dict of dicts to represent our trie nodes. 
# Key is a char and value is child nodes as a dict.
# Special key '*' contains count of contacts below this point.
trie_root_node = {}


def add_name(node, name):
    # Iter thru trie/tree nodes to find insertion point. Track count of contacts as we go.
    for char in name:
        if char not in node:
            # Insert new node with contacts counter
            node[char] = {'*': 1}
        else:
            node[char]['*'] += 1
        # Go to next node down
        node = node[char]

    return


def find_partial(node, string):
    # print 'DEBUG: ***** find =', string
    matches_count = 0
    for i, char in enumerate(string):
        # print 'char =', char
        if char not in node or '*' not in node[char]:
            # No full match found
            print 0
            return

        matches_count = node[char]['*']
        # print 'node[*] =', node['*']
        # print 'node[char] =', node[char]
        # print 'node[char][*] =', node[char]['*']
        node = node[char]

    print matches_count
    return


# BEGIN HackerRank's starter code
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')

    # BEGIN Tyler's code
    if op == 'add':
        add_name(trie_root_node, contact)
        # print 'DEBUG: tree ='
        # pprint.pprint(trie_root_node)
    else:
        find_partial(trie_root_node, contact)
