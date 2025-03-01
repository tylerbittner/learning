"""
Outco Graphs Class - 2025-02-25, with Karthik
Excalidraw notes: https://excalidraw.com/#room=1efa42c02a402424712e,iHviD5HVsshHYw4z4LQbRw

=== THEORY ===

Properties of TREES (vs. graphs):
- 1 root element
- no cycles
- Any 2 nodes are connected
- only 1 path between two nodes
- Each node has property "children" (or left/right)
- In a tree with n nodes, how many edges are there?  n-1
- More than n-1 nodes would induce a cycle

=== Depth-first search (usually use recursion): ===
- Gotcha: limited by language recursion stack limit

def dfs(root, searched_val):
    if root is None:
        return False
    # Desired value found
    if root.value == searched_val:
        return True
    # Keep searching
    return dfs(root.left, search) or dfs(root.right, search)

- Pre-order: Action,L,R
- In-order: L,Action,R
- Post-order: L,R,Action

DFS PATH:
- Input: root, search point
- Output: path thru tree
- e.g. DFS_PATH(root, 'G') -> [A,C,E,G]

def dfs_path(root, search, path):
    if root == None:
        return False
    if root.value == search:
        path.append(search)
        return path
    path.append(root.value)
    dfs(root.left, search, path)
    dfs(root.right, search, path)


=== Breadth-first search (use iteration w/ a queue): ===

** Use a parent_node dict to track parent of each node for not only easy & cheap path tracking, but
    simple conversion to graph traversal!

def bfs(root, search):      # Includes parents dict for path tracking etc.
    queue = [root]
    parents = {root: None}
    while len(queue) > 0:
        curr = queue.pop()
        if curr.value == search:
            return True
        if curr.left:
            queue.append(curr.left)
            parents[curr.left.value] = curr.value
        if curr.right:
            queue.append(curr.right)
            parents[curr.right.value] = curr.value
    path = []
TODO:
    while ...



=== LOWEST COMMON ANCESTOR Problem ===

- Given root of family tree, and two members of family, output first point from where they branched

def lca(root, member1, member2):
    # 1. Get paths to both
    path1 = bfs(root, member1)
    path2 = bfs(root, member2)

    # 2. Compare paths up to where they differ
    min_len = min(len(path1), len(path2))
    for i in range(min_len):
        if path1[i] == path2[i]:
            next
        else:
            return path1[i-1]

Time: O(V)
Space: O(V)

==============
=== GRAPHS ===
Properties:
- Number of edges E <= V^2
- Object represenation:
    graph = {
        'A': {B,C,K,D},
        'B': {E,F,G,H,C},
        ...
        }

Question: if 'D' is in graph['A'], return True, else False.  In O(1) time.
KEY: Use *visited* set!

def bfs(root, search):      # Includes parents dict for path tracking etc.
    queue = [root]
    visited = {}
    parents = {root: None}
    while len(queue) > 0:
        curr = queue.pop()
        if curr in visited:
            continue
        else:
            for neighbors in graph[curr]
                if neighbors not in parents:
                    parents[neighbors] = curr
                    queue.append(neighbors)
            visited.add(curr)
    # Get path
    path = []
    path.append(search)
    while search is not null:
        search = parents[search]
        path.append(search)
    return reverse(path)

"""
