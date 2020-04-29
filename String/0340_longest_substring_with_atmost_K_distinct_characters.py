"""
To find length of longest substring with - at-most 2 distinct characters
Technique: < SLIDING WINDOW >
"""

def length_of_longest_substring_K_distinct_sliding_window(string, k):
    # Basic sanity checks
    if not string: return 0
    if len(string) < k+1: return len(string)

    # Following Sliding Window Template
    max_length = k
    left, right = 0, 0

    seen = {} # Data Structure to manage the window condition

    for i, char in enumerate(string):
        """
        Condition-1: to keep increasing the size of the window.
        1. The number of distinct characters is not greater than 2
        2. We keep updating the char with the index we see it in
        3. Also keep incrementing the right pointer
        """
        if len(seen) < k+1:
            seen[char] = i
            right += 1

        """
        Condition-2: to decrease the size of the window
        When to decrease the size? - When we see more than 2 distinct chars
        We have to move the left pointer?
        """
        if len(seen) == k+1:
            index = min(seen.values()) 
            del seen[string[index]]
            left = index + 1

        max_length = max(max_length, right-left)

    return max_length

# -----------------------------------------------------------------
# Driver Code
input_string = "eceba"
result = length_of_longest_substring_K_distinct_sliding_window(input_string, k=2)
print("The output is:", result)