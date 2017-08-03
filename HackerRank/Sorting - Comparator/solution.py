# Problem statement: https://www.hackerrank.com/challenges/ctci-comparator-sorting


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def __repr__(self):
    #    pass

    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        else:
            # Sort scores DESCENDING
            return other.score < self.score

    def __eq__(self, other):
        if self.score == other.score:
            return self.name == other.name
        else:
            return self.score == other.score

    def comparator(a, b):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
