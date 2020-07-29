def solution(S):
    # write your code in Python 3.6
    if not S:
        return ""

    output = []
    S = [c for c in S]
    i = 0
    while i <= len(S) - 1:
        if i == len(S) -1:
            output.append(S[i])
            break
        elif S[i] == 'A' and S[i + 1] != 'B' or (S[i] == 'C' and S[i + 1] != 'D'):
            output.append(S[i])
            i += 1
        elif S[i] == 'A' and S[i + 1] == 'B' or (S[i] == 'C' and S[i + 1] == 'D'):
            i += 2
        elif S[i] == 'B' and S[i + 1] == 'A' or (S[i] == 'D' and S[i + 1] == 'C'):
            i += 2
        else:
            output.append(S[i])
            i += 1

    output = ''.join(c for c in output)

    if output == 'AB' or output == 'BA' or output == 'CD' or output == 'DC':
        return ''
    else:
        return output

res = solution('ACBDACBD')
print("The res is:", res)