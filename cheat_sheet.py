from collections import Counter
import heapq

# To sort a hash-map by value or key
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}

# To sort a hash-map by value and then by key
inp_list = []
ctr = Counter(inp_list)
# This creates a tuple, and tuple are by default sorted by value, then we set the priority
res = sorted(ctr, key= lambda x:(-ctr[x], x))

# Getting the most_common  or 'frequent' elements- Returns the tuple
arr = [1, 3, 5, 6, 7, 7, 1, 1, 2, 3]
ctr1 = Counter(arr)
top_three_frequent = ctr1.most_common(3)
print(top_three_frequent)

# Getting the top 'n' largest or top 'n' smallest
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
top_three_largest = heapq.nlargest(3, marks)
top_three_smallest = heapq.nsmallest(3, marks