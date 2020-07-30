"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict
from collections import deque


class Solution:
    def getImportance(self, employees: List['Employee'], idd: int) -> int:
        importance_map = {}
        g = defaultdict(list)

        for e in employees:
            leader = e.id
            importance_map[leader] = e.importance

            for sub in e.subordinates:
                g[leader].append(sub)

        if idd not in g.keys():
            return importance_map[idd]

        visited = set()
        q = deque([idd])
        result = importance_map[idd]
        while q:
            node = q.popleft()
            for nei in g[node]:
                if nei not in visited:
                    result += importance_map[nei]
                    visited.add(nei)
                    q.append(nei)

        return result