"""
Graph related content
"""


from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node, neighbour):
        self.graph[node].append(neighbour)

    def show_edges(self):
        for k, v in self.graph.items():
            print(k, v)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                # After recursive call-stack ends, the end will be in PATH
                if new_path:
                    return new_path
                return None

    def BFS(self, start):
        visited = {}
        result_path = []
        for k in self.graph:
            visited[k] = False

        q = deque(start)
        visited[start] = True

        while q:
            print("The queue is:", q)
            vertex = q.popleft()
            print("The vertex is:", vertex)
            for neighbours in self.graph[vertex]:
                if not visited[neighbours]:
                    visited[neighbours] = True
                    q.append(neighbours)
            result_path.append(vertex)
        return result_path

    def DFS(self, start):
        visited = {}
        result_path = []
        for i in self.graph:
            visited[i] = False

        stack = [start]
        visited[start] = True

        while stack:
            vertex = stack.pop(len(stack) - 1)
            for neighbours in self.graph[vertex]:
                if not visited[neighbours]:
                    stack.append(neighbours)
                    visited[neighbours] = True
            result_path.append(vertex)
        return result_path

g = Graph()

g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '3')
g.add_edge('2', '1')
g.add_edge('3', '1')
g.add_edge('3', '2')
g.add_edge('3', '4')
g.add_edge('4', '3')




print("Showing the edges")
g.show_edges()

"""
flow = g.find_path('4', '1')
print(flow)
"""
result = g.BFS('1')
print("BFS", result)

result = g.DFS('1')
print("DFS", result)

path = g.find_path(5, 3)


# Other things to learn
"""
1. Djikstra shortest path 
2. Floyd Warshall - shortest path from every vertex to every other vertex
3. Prim / Kruskal - Minimum Spanning Tree

DFS Applications

1. Detecting cycle in a graph
2. Path finding
3. Topological sort
4. Testing if a graph is bi-partite

BFS Applications
1. Shortest path / MST for unweighted graph
2. Cycle detection in undirected / directed graph
3. Testing if a graph is bi-partite
4. Path finding b/w 2 vertices
5. Finding all nodes within one connected component.
   to find all nodes reachable from a given node.

Another technique to learn is Union-Find - Need to know what that technique is.

Other representations of graph are:
1. adjacency matrix
we generally use adjacency matric if we know that the number of edges is
higher than the number of nodes.

2. linked representation
here, we make actual node objects, not commonly used in interviews
"""

# Check cycle in undirected graph
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Constructing the Graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            # print("The node is:", node)
            for neighbour in graph[node]:
                # print("the neighbor is:",neighbour)
                if neighbour == parent[node]:
                    continue
                # if node is in the parent hashmap but is not your direct parent
                if neighbour in parent:
                    # print("Entering here")
                    return False
                parent[neighbour] = node
                stack.append(neighbour)

                # print(parent)
            # print("************")

        return len(parent) == n

# Clean Smarter solution
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1: return False

    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    stack = [0]

    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            stack.append(neighbour)

    return len(seen) == n

### Just to check if you have parsed everything
from collections import defaultdict
from collections import deque


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Generating the Graph
        for i, c in enumerate(rooms):
            for d in c:
                self.graph[str(i)].append(str(d))

        # Just do regular DFS / BFS traversal, and see if we can vist all nodes.
        visited = {}
        start = '0'

        for k in range(len(rooms)):
            visited[str(k)] = False

        q = deque(start)
        visited[start] = True

        while q:
            vertex = q.pop()  # DFS
            #	vertex = q.popleft() # BFS
            for neighbour in self.graph[vertex]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    q.append(neighbour)

        val = visited.values()

        if all(c for c in val):
            return True
        return False

# BFS / DFS on all nodes templates

### To check if Graph is Bi-partite or not
from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        for i, c in enumerate(graph):
            adj_map[i] = c
        print(adj_map)

        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] == -1:
                color[start] = 0
                stack = [start, ]

                while stack:
                    parent = stack.pop()

                    for child in adj_map[parent]:
                        if color[child] == -1:
                            color[child] = 1 - color[parent]
                            stack.append(child)
                        elif color[parent] == color[child]:
                            return False, color
        return True, color