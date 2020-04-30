"""
Remove an element from an array in-place
"""

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
        return len(nums)