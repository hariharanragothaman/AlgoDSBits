def find_median_of_sorted_arrays(nums1, nums2):
    values = sorted(nums1+nums2)
    length = len(values)
    index = (length - 1) // 2

    if length % 2 != 0:
        return values[index]
    else:
        return (values[index] + values[index+1]) / 2.0


nums1 = [1, 2]
nums2 = [3, 4]
nums3 = [1]

# odd case
result = find_median_of_sorted_arrays(nums3, nums2)
print("the median is:", result)

# even case
result = find_median_of_sorted_arrays(nums1, nums2)
print("the median is:", result)