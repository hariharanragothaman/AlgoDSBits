from collections import defaultdict

stock_data = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
queries = [6, 5, 4]

hash_map = defaultdict(list)

for i in range(len(stock_data)):
    hash_map[stock_data[i]].append(i)
print(hash_map)

hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])}
print("The sorted hash_map is:", hash_map)

keys = list(hash_map.keys())
result = []

for i in range(len(queries)):
    idx = queries[i] - 1
    value = stock_data[idx]
    print("The value is:", value)
    candidates = keys[:keys.index(value)]
    print("The candidates are:", candidates)

    ## Binary Search recipe - keys

    left, right = 0, len(candidates) - 1
    while left < right:
        mid = (left + right) // 2
        if value - candidates[mid] > candidates[mid+1] - value:
            left = mid + 1
        else:
            right = mid

    print("The value of left is:", left)
    idx_can = candidates[left]
    print("The indexes to see are:", hash_map[idx_can])

    idxes = hash_map[idx_can]

    if len(idxes) == 1:
        result.append(idxes[0] + 1)
    else:
        min_value, temp = float('inf'), float('inf')
        for i in range(len(idxes)):
            if abs(idxes[i] - idx) < min_value:
                min_value = abs(idxes[i] - idx)
                temp = idxes[i]
        if temp != float('inf'):
            result.append(temp+1)
        else:
            result.append(-1)
    print("The result is:", result)
    print("********************************************")