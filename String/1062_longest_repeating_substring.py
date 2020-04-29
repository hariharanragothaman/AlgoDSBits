"""
Problem: Given a string - return the length of the longest substring, that repeats
Solution: There are definitely better solutions than this, since this is O(n^2)
          This generates all possible sub-strings
"""

def longestRepeatingSubstring(S):
    hmap = {}
    max_length = 0

    # This generates all possible sub-strings
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            substr = S[i:j]

            if substr in hmap:
                hmap[substr] += 1
                # If it's a repeated sub-string - we update max_length
                max_length = max(max_length, len(substr))
            else:
                hmap[substr] = 1
    return max_length

input_string = "abbaba"
input_string2 = "abcd"
length = longestRepeatingSubstring(input_string)
print("The length is:", length)