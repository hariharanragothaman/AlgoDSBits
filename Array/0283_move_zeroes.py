"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i, data in list(enumerate(nums)):
        if data == 0:
            nums.remove(data)
            nums.append(0)