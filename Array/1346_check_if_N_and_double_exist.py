def check_double(arr):
    if arr.count(0) > 1:
        return True
    for i, c in enumerate(arr):
        if c * 2 in arr and c != 0:
            return True
    return False


arr = [10, 2, 5, 3]
arr2 = [0, 0]
arr3 = [1, 2, 3, 0]
output = check_double(arr3)
print("The O/P is:", output)