from collections import Counter

# To sort a hash-map by value or key
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}

# To sort a hash-map by value and then by key
inp_list = []
ctr = Counter(inp_list)
# This creates a tuple, and tuple are by default sorted by value, then we set the priority
res = sorted(ctr, key= lambda x:(-ctr[x], x))
