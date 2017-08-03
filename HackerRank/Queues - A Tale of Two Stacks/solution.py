# Problem statement: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks


from collections import deque


class MyQueue(object):
    def __init__(self):
        # self.first = []
        # self.second = []    # Why the hell are we being asked to use 2 stacks??
        self.first = deque([])
        self.second = deque([])

    def peek(self):
        return self.first[0]

    def pop(self):
        return self.first.popleft()

    def put(self, value):
        self.first.append(value)
        return


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()

