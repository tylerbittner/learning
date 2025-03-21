'''
Sliding Window
(with Ari Saif) :)

CLASS NOTES: https://docs.google.com/document/d/1Yt8GKSLhNioomd7l8VSqbduAxj-B4xci5F2CjzodtYE/edit?usp=sharing

What is the Sliding Window technique?
- Optimization technique used to reduce time complexity of problems involving
    lists/arrays/strings by avoiding unnecessary computation
- Often O(n) runtime
- Unoptimized versions of problems are usually O(n^2)
- Two kinds of windows:
    1. fixed size (we only need one pointer in this case)
    2. variable size (need left & right)

How does it work?
1. Init window using left/right pointers
2. Expand to include new elements (move right)
3. Shrink when necessary (move left)
4. Update result based on problem

Indicators to use sliding window for a problem:
- Should require a contiguous sequence fo list
- Usually, result should change monotonically if variable size window is used
    - E.g. as window changes size, result should either always increase or decrease
    - We're usually minimizing or maximizing the length of subarray with some property

How do I solve a SW problem?
1. Identify problem type:
    1. recognize whether the property we're looking for is changing monotonically or not
    2. determine whether fixed or variable size window is needed
2. Init the window with two pointers: left & right
    - l = 0, r = 0
    - Expand: increase r until condition is violated (e.g. at end of list)
3. Adjust window based on conditions:
    - If condition is true, expand (l++)
    - Otherwise expand right (r++)
    -...
    - Note sometimes L can jump to r's position
TEMPLATE SW SOLUTION:
...

'''

'''
Example problem:
    Given a string, find the shortest contiguous substring that contains at least 3 unique characters.
    If no such substring exists, return an empty string.
Ex 1: 
    s = 'abcabc'
    solution: 'abc'
Ex 2: 
    s = 'aabbcc'
    solution: 'abbc'

Solution options:
1. Brute force: check all possible substrings O(n^2)
2. Sliding window: Note monotonic property: as the window size increases the # of unique chars increases or stays same.
    1. create window
    2. store result
    2. adjust window state
'''
from collections import defaultdict
def shortest_with_e_unique(s):
    l = 0
    result = ''
    chars_seen = defaultdict(int)
    min_size = float('inf')

    for r in range(len(s)):
        # Update state: track chars in window
        chars_seen[s[r]] += 1

        # If we have at least 3 unique chats, this window is a candidate. Store in result.
        while len(chars_seen.keys()) >= 3:
            ...


    pass

# Write tests...

'''
Problem 2: Leetcode 424. Longest repeating character replacement
*** A commonly-seen problem apparently!


Confusingly worded.  In other words, the problem wants "after performing at most k changes, 
the entire substring should consist of only one repeating character"

'''

