"""
Given a string, display in zig-zag order, given the number of rows
Sample: "PAYPALISHRING"

P   A   H   N
A P L S I I G
Y   I   R

Reading line ny line, Final O.P: PAHNAPLSIIGYIR"
"""


def zigzag(string, rows):
    if rows == 1 or rows >= len(string):
        return string

    output = [''] * rows

    index = 0
    step = 1

    for char in string:
        output[index] += char

        # logic to go and back and forth in O/P - based on zig-zag pattern
        if index == 0:
            step = 1
        elif index == rows - 1:
            step = -1

        index += step

    # Finally returning the O/P
    return ''.join(c for c in output)


string = "PAYPALISHIRING"
result = zigzag(string, 3)
print("The zig-zag pattern is:", result)