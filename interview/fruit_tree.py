
fruit = ['A', 'B', 'C', 'A', 'C']
fruit2 = ['A', 'B', 'C', 'B', 'B', 'C']
fs = ''.join(c for c in fruit)
print(fs)

# This problem can be essentially rephrased as
# the longest substring that contains only 2 distinct characters

def find_max_sum(fruit, k=2):
    fs = ''.join(c for c in fruit)
    if not fs:
        return 0
    if len(fs) < k+1:
        return len(fs)

    max_length = k
    left, right = 0, 0

    seen = {}

    for i, char in enumerate(fs):
        if len(seen) < k+1:
            seen[char] = i
            right += 1

        if len(seen) == k+1:
            index = min(seen.values())
            del seen[fs[index]]
            left = index + 1
        max_length = max(max_length, right-left)

    return max_length



s1 = find_max_sum(fruit2)
print(s1)