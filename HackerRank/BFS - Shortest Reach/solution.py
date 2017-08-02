from collections import deque

class Graph:
    """Represents a graph data structure.
    NOTE: A zero-based index is used internally in the graph, but add 1 when printing labels as
    they are 1-based."""

    def __init__(self, n):
        """ Init graph as adjacency list with connected nodes as a list"""

        self.graph = [[] for i in xrange(n)]

    def connect(self, u, v):
        """Add an undirected edge from node u to node v"""

        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_all_distances(self, start_node):
        """Print list of distances from source node s to all other nodes"""

        distances = [-1] * len(self.graph)

        # Do BFS
        # Init queue with start node
        queue = deque()
        queue.append(start_node)
        distances[start_node] = 0
        while queue:
            node = queue.popleft()
            for child in self.graph[node]:
                # There may be multiple paths to a node so only process nodes we have NOT seen yet
                if distances[child] == -1:
                    distances[child] = distances[node] + 6
                    queue.append(child)

        # Output solution as dictated. Don't print distance to start node
        del distances[start_node]
        for d in distances:
                print d,
        print


# HackerRank's template code
t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for j in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        # Tyler's note: Looks like they are assuming a zero-based array will be used as an adjacency list
        graph.connect(x - 1, y - 1)
    s = input()
    # Tyler's note: also assumes a zero-based array is used
    graph.find_all_distances(s - 1)
