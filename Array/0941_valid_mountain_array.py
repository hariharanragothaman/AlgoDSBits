"""
Given an array A of integers, return true if and only if it is a valid mountain array.
"""


def valid_mountain_array(array):
    if len(array) < 3:
        return False

    peak = max(array)
    pindex = array.index(peak)

    # Splitting the mountain
    fp = array[:pindex]
    sp = array[pindex + 1:]

    """
    Scenario's of False
    1. If either fp or sp is empty -> both are increasing / decreasing array
    2. If there is only one element in fp / sp after split and they are equal to peak element
    3. Parse through the array, check for duplicates and non-following mountain pattern

    """

    if (len(fp) == 1 and fp[0] == peak) or (len(sp) == 1 and sp[0] == peak) or not sp or not fp:
        return False

    for i in range(1, len(fp)):
        if fp[i] == fp[i - 1] or fp[i] < fp[i - 1]:
            return False

    for i in range(1, len(sp)):
        if sp[i] == sp[i - 1] or sp[i] > sp[i - 1]:
            return False

    return True


input_list = [5, 4, 3, 2, 1]
input_list2 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
result = valid_mountain_array(input_list2)
print(result)