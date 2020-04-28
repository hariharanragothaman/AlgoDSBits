"""
Modification to the previous problem:
Given a list of strings - find the longest uncommon sequence
"""


def longest_uncommon_subsequence(input_list):
    def is_subsequence(s, t):
        t = iter(t)
        return all(c in t for c in s)

    input_list = sorted(input_list, key=len, reverse=True)
    # one of the important test cases here, to if members of your lists are not subsequences
    for string in input_list:
        if sum(is_subsequence(string, t) for t in input_list) == 1:
            return len(string)
    return -1


input_list = ["aba", "cdc", "eae"]
length = longest_uncommon_subsequence(input_list)
print("The length of the longest uncommon subsequence is:", length)

