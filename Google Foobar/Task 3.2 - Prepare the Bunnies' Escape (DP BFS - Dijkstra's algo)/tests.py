import unittest
# My code
from solution import answer


class TestAlgo(unittest.TestCase):

    def test_answer_provided1(self):
        maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
        self.assertEqual(answer(maze), 7)

    def test_answer_provided2(self):
        maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(answer(maze), 11)

    def test_answer_basic(self):
        self.assertEqual(answer([[0 for cols in xrange(2)] for rows in xrange(2)]), 3)
        self.assertEqual(answer([[0 for cols in xrange(4)] for rows in xrange(4)]), 7)
        self.assertEqual(answer([[0 for cols in xrange(20)] for rows in xrange(20)]), 39)
        self.assertEqual(answer([[0 for cols in xrange(2)] for rows in xrange(20)]), 21)
        self.assertEqual(answer([[0 for cols in xrange(20)] for rows in xrange(2)]), 21)

    def test_answer_simple_wall(self):
        maze = [[0 for cols in xrange(2)] for rows in xrange(2)]
        maze[0][1] = 1
        self.assertEqual(answer(maze), 3)

    def test_answer_walls_not_in_path(self):
        maze_20x20_walls_no_problem = [[0 for cols in xrange(20)] for rows in xrange(20)]
        maze_20x20_walls_no_problem[1][0] = 1
        maze_20x20_walls_no_problem[0][2] = 1
        self.assertEqual(answer(maze_20x20_walls_no_problem), 39)

    def test_answer_walls_blocking_path(self):
        maze = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
        self.assertEqual(answer(maze), 5)

    def test_answer_backwards_walk(self):
        maze = [[0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 0]]
        self.assertEqual(answer(maze), 31)

    # def test_answer_(self):
        # self.assertEqual(answer(''), )


if __name__ == '__main__':
    unittest.main(verbosity=2)
