""""
Problem statement: Given an input string, reverse the string word by word.

Input: "the sky is blue"
Output: "blue is sky the"

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""
def reverse_sentence(string):
    strs = string.split()[::-1]
    return ' '.join(c for c in strs)

input1 = "the sky is blue"
output = reverse_sentence(input1)
print("The O/P is:", output)

input2 = " hello world!"
output = reverse_sentence(input2)
print("The O/P is:", output)

input3 = "a good    example"
output = reverse_sentence(input3)
print("The O/P is:", output)