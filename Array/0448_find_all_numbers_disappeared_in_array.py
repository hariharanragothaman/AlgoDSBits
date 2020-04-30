"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""

from collections import Counter
from collections import defaultdict


def find_disappeared_numbers(nums):
    """
    Method1:

    result = [c for c in range(1, len(nums)+1) if c not in set(nums)]
    return result
    """

    """
    Method2:

    ctr = Counter(nums)
    rge = list(range(1, len(nums)+1))
    return [c for c in rge if c not in list(ctr.keys())]
    """

    hashmap = {}
    for i in range(1, len(nums) + 1):
        hashmap[i] = 0

    for n in nums:
        hashmap[n] += 1

    hashmap = {k: v for k, v in hashmap.items() if v == 0}
    return list(hashmap.keys())