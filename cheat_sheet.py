"""
Things to use frequently and master
list, deque, set, dict, defaultdict, heapq, sorted, bisect, itertools, functools, reduce, map, random
pypi modules - pyavl, rbtree - for self balancing BST

"""

from collections import Counter
import heapq
import itertools

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
list1 = [[1,2,3], [4,5,6],[7,8,9]]
flt = list(itertools.chain.from_iterable(list1))


# Let's say you zip 2 objects - you can convert them into a hashmap easily
t1 = (1, 2, 3)
t2 = (4, 5, 6)
# { 1:4 , 2:5, 3:6 }
op = dict(zip(t1, t2))

# To find all factors of a number in python
from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Lambda Basic Example
add = lambda x, y : x + y
add(4, 5)

# Writing an if-else in one-line
# [if_true] if [condition] else [if_false]
y = 20
x = 5 if y > 10 else 25

# ------------------------------------------------------------------------------------------------------------------
"""
2-D Matrices Hacks
"""
# Getting Transpose of 2D matrix - Basically gets all the columns - makes it as rows
matrix[:] = zip(*matrix)

# Rotating a 2D matrix - Basically do transpose and reverse each row
matrix[:] = zip(*matrix[::-1])


# To get the rows of a matrix
def get_rows(matrix):
    return [[c for c in r] for r in matrix]

# To get the columns of a matrix
def get_columns(matrix):
    return zip(*matrix)
