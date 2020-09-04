
"""
def solution(N):
    # write your code in Python 3.6
    char = 'L'
    for i in range(N-1):
        print("L")
    print(char * N)

solution(4)

def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1





"""

def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1

    print(d)
    print(l)
    for p in range(1, l):
        ok = False
        for i in range(l - p):
            if d[i] == d[i + p]:
                ok = True
        if ok:
            return p
    return -1

result = solution(547)
print(result)