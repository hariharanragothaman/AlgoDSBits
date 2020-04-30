"""
Return the 3rd maximum number in a given array
"""

def thirdMax(self, nums: List[int]) -> int:
    """
    1. First, get rid of duplicates
    2. Sort the array
    3. if length is < 3 - return the last element
    4. Else reverse sort and return the arr[2]

    """
    nums = list(set(nums))

    if len(nums) < 3:
        return sorted(set(nums))[-1]
    else:
        res = sorted(nums, reverse=True)
        return res[2]