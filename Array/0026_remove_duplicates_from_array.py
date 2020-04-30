"""
Remove duplicates from an array-in-place which is sorted
"""

# Method 1 : Regular
def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)