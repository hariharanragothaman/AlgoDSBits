"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note: that an empty string is also considered valid.
"""

def is_valid_parentheses(string):
    stack = []
    opened = ['(', '{', '[']
    closed = [')', '}', ']']

    for i, c in enumerate(string):
        if c in opened:
            stack.append(c)
        elif c in closed:
            index = closed.index(c)
            if stack and stack[-1] == opened[index]:
                stack.pop()
            else:
                return False
        print("The stack currently is:", stack)

    if not stack:
        return True


ip1 = "()"
ip2 = "()[]{}"
ip3 = "(]"
ip4 = "([)]"
ip5 = "{[]}"
ip6 = "["

isvalid = is_valid_parentheses(ip1)
print("The string is:", isvalid)