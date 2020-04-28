"""
To return the "length" of the longest sub-string without repeating characters
< SLIDING WINDOW >
"""

def longest_substring_without_repeat_chars(string):
    # Maintaining 2 pointers in the sliding window
    left, right = 0, 0
    max_length = 0

    # Since Q is about - non-repeating, use hash-map or set()
    seen = {}

    for i, char in enumerate(string):
        # character has never been seen before (or)
        # character is 'behind' and not part of the current window - Eg: "tmmzuxt"
        if char not in seen or seen[char] < left:
            right = i  # increase the window
            seen[char] = i

            if (right-left+1) > max_length:
                max_length = (right-left+1)

        else:
            # character is getting repeated - contract the window
            left = seen[char] + 1 # - move left pointer one step ahead of the repeated char
            seen[char] = i

    return max_length

string = "abcabcbb"
string2 = "tmmzuxt"

output = longest_substring_without_repeat_chars(string2)
print("The max length is:", output)