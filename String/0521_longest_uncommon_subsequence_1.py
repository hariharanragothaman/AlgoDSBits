"""
Q: Given 2 strings, find the longest uncommon subsequence

Solution:
This is just the length of the longest string in the I/P
Initially had thought about uncommon characters and so on.
"""
def longest_uncommon_subsequence(string1, string2):
    if string1 == string2:
        return -1
    else:
        return max(len(string1), len(string2))