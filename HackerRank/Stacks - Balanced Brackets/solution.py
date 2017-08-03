# Problem statement: https://www.hackerrank.com/challenges/ctci-balanced-brackets


def is_matched(expression):
    # print expression

    # Chars must be even-numbered to be balanced
    if not len(expression) % 2 == 0:
        return False

    stack = []
    for char in expression:
        # If an opener, push to stack
        if char in '{[(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            # If closer is balanced w/ an opener, remove its match
            if balanced(stack[-1], char):
                stack.pop()
            else:
                return False

    # Finally, if anything left in the stack it's unbalanced
    if len(stack) > 0:
        return False

    return True


def balanced(top_char, char):
    openers = '{[('
    closers = '}])'
    if openers.index(top_char) == closers.index(char):
        return True
    return False


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
