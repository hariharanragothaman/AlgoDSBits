def longest_substring_palindrome(string):
    palindrome = ''

    # Remember this template:
    # @ Maintain 2 pointers - one pointer, starts from the beginning
    # Another pointer starts from the end
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if len(palindrome) > j-i:
                break
            elif string[i:j] == string[i:j][::-1]:
                palindrome = string[i:j]
    return palindrome

string = "babad"
result = longest_substring_palindrome(string)
print("The longest palindromic substring is:", result)