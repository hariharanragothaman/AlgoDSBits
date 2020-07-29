"""
Things to use frequently and master
list, deque, set, dict, defaultdict, heapq, sorted, bisect, itertools, functools, reduce, map, random
pypi modules - pyavl, rbtree - for self balancing BST

# Famous algorithms to remember and know very well.....
1. Kadanee's algorithm - maximum sum sub-array
2. Manchester's algorithm
3. Floyd Warshall 2-pointer technique
4. Lowest Common Ancestor in a B-Tree and BST
4. Moving Average in a stream - using a queue
4. Maximum Subarray - Kadane's algorithm -
5. subarray equal K - Cumulative sum
"""


from collections import Counter
from collections import OrderedDict

import heapq
import itertools

"""
General Important Hacks
"""

# To sort a hash-map by value or key
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}

# To sort a hash-map by value and then by key
inp_list = []
ctr = Counter(inp_list)
# This creates a tuple, and tuple are by default sorted by value, then we set the priority
res = sorted(ctr, key=lambda x: (-ctr[x], x))

# Getting the most_common  or 'frequent' elements- Returns the tuple
arr = [1, 3, 5, 6, 7, 7, 1, 1, 2, 3]
ctr1 = Counter(arr)
top_three_frequent = ctr1.most_common(3)
print(top_three_frequent)

# Getting the top 'n' largest or top 'n' smallest
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
top_three_largest = heapq.nlargest(3, marks)
top_three_smallest = heapq.nsmallest(3, marks)

# Flatten a list of lists
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flt = list(itertools.chain.from_iterable(list1))
flat_list = [item for sublist in list1 for item in sublist]

# Usage of all()
# It takes an iterable and returns if the contents of the iterable is True
samples = [5, 6, 7, 8, 9]
check = all(c for c in samples if c > 5)
print(check)

# Let's say you zip 2 objects - you can convert them into a hashmap easily
t1 = (1, 2, 3)
t2 = (4, 5, 6)
# { 1:4 , 2:5, 3:6 }
op = dict(zip(t1, t2))

# To find all factors of a number in python
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


# Lambda Basic Example
add = lambda x, y: x + y
add(4, 5)

# Writing an if-else in one-line
# [if_true] if [condition] else [if_false]
y = 20
x = 5 if y > 10 else 25

# Kadane's algorithm
# Kadane's algorithm
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
max_sum = nums[0]

for i in range(1, n):
    if nums[i - 1] > 0:
        nums[i] += nums[i - 1]
    max_sum = max(nums[i], max_sum)

print(max_sum)

# ------------------------------------------------------------------------------------------------------------------
"""
2-D Matrices Hacks
"""
# Getting Transpose of 2D matrix - Basically gets all the columns - makes it as rows
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[:] = zip(*matrix)

# Rotating a 2D matrix - Basically do transpose and reverse each row
matrix[:] = zip(*matrix[::-1])


# To get the rows of a matrix
def get_rows(matrix):
    return [[c for c in r] for r in matrix]


# To get the columns of a matrix
def get_columns(matrix):
    return zip(*matrix)


# ------------------------------------------------------------------------------------------------------------------
"""
String related hacks
"""


# Check if 's' is a subsequence of t - Method1
def is_sub_sequence(s, t):
    for i in range(len(s)):
        try:
            index = t.index(s[i])
        except ValueError:
            return False
        t = t[index + 1:]
    return True


# A smarter way of doing this.
def is_sub_sequence2(s, t):
    t = iter(t)
    # Here 'c in t' is a condition
    # if it's false - for one of the char is not found.
    # iter - takes care of it - next()
    return all(c in t for c in s)


# --------------------------------------------------------------------------------------------------------------------
"""
Ordered Dictionary - OrderedDict
Methods to know are: 
1. move_to_end(value) - Moved the value to the end of the dict 
2. popitem() - popitem(last=True) if True - LIFO, else FIFO
"""

inp = "leetcodeisawesome"
ctr = OrderedDict(Counter(inp))
print(ctr)

# ------------------------------------------------------------------------------------------------------

# STACK & BFS || Queue and DFS

# This is the Level-Order Traversal template (BFS)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root: return 0

        q = deque([root])
        storage = []

        while q:
            storage.append([])

            for i in range(len(q)):
                node = q.popleft()
                storage[depth].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # print("The queue is:", q)
            # print("The storage is:", storage)
            depth += 1

        return depth

# A neat trick we learnt: - These 2 are equivalent
# WOW - Just wow

queue += filter(None, (node.right, node.left))

if node.right:
    queue += [node.right]
if node.left:
    queue += [node.left]

# DFS - template - And this is Pre-order Traversal
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
             2
            / \
           1   3
            \
             4
        """
        result = []
        if root is None:
            return result

        stack = [root, ]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)

                # root - left - right
                # what you want after, root, append at last in the stack.
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

# PostOrder is just reverse of Pre-order - Wow. Good
#Inorder Traversal of the BST yields a sorted array.cd cd

# To generate all possible sub-strings
for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
        print(nums[i:j])

# using the 'end' as a seperator while printing
print(val, end="")

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)