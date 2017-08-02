#
# Commander Lambda # 3.2: Prepare the Bunnies' Escape
# Solution by J. Tyler Bittner (tylerbittner@gmail.com)
#
import sys
from heapq import heappush, heappop
from copy import deepcopy


class Graph:
    """Represents graph of connected Nodes.  Nodes are indexed in graph same as the maze coordinates."""

    def __init__(self, maze):
        """Init & build graph"""

        self.maze = maze
        # Init matrix to store Node objects
        self.nodes = deepcopy(maze)

        # Init Nodes
        for row in xrange(len(maze)):
            for col in xrange(len(maze[0])):
                node = Node(row, col, maze[row][col])
                self.nodes[row][col] = node

    def get_nodes(self):
        return self.nodes

    def get_neighbors(self, node):
        """Returns list of valid neighbors of given node.  'Valid' means row/col indexes are within maze boundaries,
        not a wall, and not visited yet."""

        neighbors = []
        # Up
        if node.row - 1 >= 0:
            candidate = self.nodes[node.row - 1][node.col]
            if self.validate_neighbor(candidate):
                neighbors.append(candidate)
        # Down
        if node.row + 1 < len(self.maze):
            candidate = self.nodes[node.row + 1][node.col]
            if self.validate_neighbor(candidate):
                neighbors.append(candidate)
        # Left
        if node.col - 1 >= 0:
            candidate = self.nodes[node.row][node.col - 1]
            if self.validate_neighbor(candidate):
                neighbors.append(candidate)
        # Right
        if node.col + 1 < len(self.maze[0]):
            candidate = self.nodes[node.row][node.col + 1]
            if self.validate_neighbor(candidate):
                neighbors.append(candidate)

        return neighbors

    @staticmethod
    def validate_neighbor(node):
        return True if (not node.is_visited() and not node.is_wall()) else False


class Node:
    """Represents a node in the graph"""

    def __init__(self, row, col, wall):
        self.row = row
        self.col = col
        self.wall = True if wall else False
        self.distance = sys.maxint
        self.visited = False

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def is_wall(self):
        return self.wall

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def is_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited


def answer(maze):
    """Calls method to find shortest path through maze."""

    shortest_path = sys.maxint

    # First look for shortest path with no walls removed
    distance = find_shortest_path(maze)
    if distance < shortest_path:
        shortest_path = distance

    # Then look for shortest path with each wall node removed, one at a time
    for row in xrange(len(maze)):
        for col in xrange(len(maze[0])):
            if maze[row][col] == 1:
                maze_modified = deepcopy(maze)
                maze_modified[row][col] = 0
                distance = find_shortest_path(maze_modified)
                if distance < shortest_path:
                    shortest_path = distance

    # Note: The above naive wall removal algo could be optimized if needed.  E.g.:
    #   - Skip removal if node is fully surrounded by walls and/or maze boundary
    #   - Instead of doing deepcopy() every time modify node.is_wall() in already-built graph

    return shortest_path


def find_shortest_path(maze):
    """Return length of shortest path thru matrix from start (upper left) to end (lower right), removing up to one 
    wall node blocking path.  Uses Dijkstra's algorithm."""

    shortest_path = sys.maxint
    graph = Graph(maze)

    # Set distance of start node
    node = graph.get_nodes()[0][0]
    node.set_distance(0)

    # Store distances in min heap.  Values are tuples of (distance, Node) so they get sorted by distance.
    distances = [(node.get_distance(), node)]
    while distances:
        node = heappop(distances)[1]
        node.set_visited(True)

        # Check whether we're at end node
        if node.get_row() == len(graph.get_nodes()) - 1 and node.get_col() == len(graph.get_nodes()[0]) - 1:
            shortest_path = node.distance + 1
            break

        for neighbor in graph.get_neighbors(node):
            new_dist = node.get_distance() + 1
            if new_dist < neighbor.get_distance():

                # If updating a node already in heap remove it first
                remove_key = (neighbor.get_distance(), neighbor)
                if remove_key in distances:
                    distances.remove(remove_key)

                neighbor.set_distance(new_dist)
                heappush(distances, (neighbor.get_distance(), neighbor))

    return shortest_path

if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    answer(maze)
