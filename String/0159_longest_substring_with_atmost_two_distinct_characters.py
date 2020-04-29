"""
Given a string, find the length of the longest substring & that has at-most 2 distinct characters
Technique used: < SLIDING WINDOW >
"""
from collections import Counter

# Solution-1: O(n^2) solution
def length_of_longest_substring_two_distinct(S):
    # Basic Sanity Check
    if not S:
        return 0

    max_length = 0

    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            # Generating the sub-string
            substr = S[i:j]
            # Check if it has atmost 2 distinct characters
            ctr = Counter(substr)
            if len(list(ctr.keys())) <= 2:
                max_length = max(max_length, len(substr))
    return max_length

# Solution-2 <SLIDING WINDOW>  - Recommended Solution
"""
To find length of longest substring with - at-most 2 distinct characters
How to implement sliding window?
"""

def length_of_longest_substring_two_distinct_sliding_window(string):
    # Basic sanity checks
    if not string: return 0
    if len(string) < 3: return len(string)

    # Following Sliding Window Template
    max_length = 2
    left, right = 0, 0

    seen = {} # Data Structure to manage the window condition

    for i, char in enumerate(string):
        """
        Condition-1: to keep increasing the size of the window.
        1. The number of distinct characters is not greater than 2
        2. We keep updating the char with the index we see it in
        3. Also keep incrementing the right pointer
        """
        if len(seen) < 3:
            seen[char] = i
            right += 1

        """
        Condition-2: to decrease the size of the window
        When to decrease the size? - When we see more than 2 distinct chars
        We have to move the left pointer?
        """
        if len(seen) == 3:
            index = min(seen.values())
            del seen[string[index]]
            left = index + 1

        max_length = max(max_length, right-left)

    return max_length

# -----------------------------------------------------------------
# Driver Code
input_string = "eceba"
result = length_of_longest_substring_two_distinct(input_string)
print("The output is:", result)

result2 = length_of_longest_substring_two_distinct_sliding_window(input_string)
print("The output is:", result2)
