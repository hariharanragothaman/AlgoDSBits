from collections import deque


def solution(A):
    # write your code in Python 3.6
    """
    There is a problem here, since the UI is not allowing me to run the code
    and is only presenting languages - English, Chinese etc.

    """
    N = len(A)
    visited = [False] * N

    hashmap = {}
    for i in range(len(A)):
        hashmap[i] = A[i]
    q = deque([0])
    length = 0

    while q:
        node = q.popleft()
        nei = hashmap[node]
        if nei == -1:
            break
        if visited[nei] is False:
            visited[nei] = True
            length += 1
            q.append(nei)

    return length + 1

A = [1, 4, -1, 3, 2]
result = solution(A)
print("The result is:", result)