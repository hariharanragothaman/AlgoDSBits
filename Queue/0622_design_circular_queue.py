"""
Queue Implementation - Detailed explanation in python
"""
# First covering the basics of Queue
# Queue can be used from regular Queue class or from collections.

from collections import deque
q = deque()

# appending elements to the right side of the queue
q.append(5)
q.append(234)
q.append(576)
cnt = q.count(5)
print(cnt)

# Extend takes an iterable
# extend - adds elements to the right
q.extend([10])
print(q)

# adds element to the left
q.extendleft([15])
print(q)

# insert num at given index
q.insert(1, 7)
print(q)

# return an element from the right side of the queue
# pop also takes index as an argument like a regular list
removed_element = q.pop()
print(removed_element)
print(q)

# popleft() removes from left side of the queue - essentially in the order of service
removed_element = q.popleft()
print(removed_element)
print(q)

print(sum(q))
print(len(q))
# Note: It also supports functions like, reverse(), reversed(), rotate() and len() and is subscriptable.

#---------------------------------------------------------------------------------------------------------

"""
Learning the various deque- recipes.
"""
# Bounded length queues can provide functionality of tail filter in Unix

def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)

# Another approach to using deque is to maintain a sequence of recently added elements
# By appending to the right and popping from the left.









