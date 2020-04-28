"""
Question: Given a list, find 2 numbers that add up to a target
"""

# This is the O(n^2) solution
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution2:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map and hash_map[diff] != i:
                return [i, hash_map[diff]]

nums = [2,7,11,15]
target = 9

s = Solution2()
result = s.twoSum(nums, target)
print("The indexes are:", result)