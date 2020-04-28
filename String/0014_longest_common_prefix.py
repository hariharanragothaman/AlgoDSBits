"""
Given multiple strings, find the longest common prefix

input_strings = ["flower", "flow", "flight"]
output = "fl"

"""

def longest_common_prefix(input_list):
    # This is basically grouping all the first, second, third letters and so on...
    # Pretty much how the human mind does..
    prefixes = (list(zip(*input_list)))
    result = ""

    for data in prefixes:
        if len(set(data)) == 1:
            result += data[0]
        else:
            # break when we reach a point where it's not matching
            break

    return result


input_list = ["flower", "flow", "flight"]
long_common_prefix = longest_common_prefix(input_list)
print("The longest common prefix is:", long_common_prefix)