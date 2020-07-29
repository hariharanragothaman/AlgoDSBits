def binary_gap(n):
    string = bin(n).replace('0b', '')
    print(string)
    hmap = {}
    max_length = 0
    for i in range(len(string)):
        if string[i] == '1':
            hmap[i] = string[i]
    print(hmap)

    keys = list(hmap.keys())
    for i in range(1, len(keys)):
        max_length = max(max_length, keys[i]-keys[i-1])

    return max_length


result = binary_gap(1041)
print(result)