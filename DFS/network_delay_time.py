from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def djikstra(self, n, graph, start):
        # Creating the distance-map & parents_map
        vertex = list(range(1, n + 1))
        distance = [float('inf')] * n
        initial_parents = [-1] * n

        distance_map = dict(zip(vertex, distance))
        parents_map = dict(zip(vertex, initial_parents))

        distance_map[start] = 0
        queue = [(0, start)]

        while queue:
            path_length, vertex = heappop(queue)
            if path_length == distance_map[vertex]:
                for nei, edge_length in graph[vertex]:
                    if edge_length + path_length < distance_map[nei]:
                        distance_map[nei] = edge_length + path_length
                        parents_map[nei] = vertex
                        heappush(queue, ((edge_length + path_length), nei))

        return distance_map, parents_map

    def networkDelayTime(self, times: List[List[int]], n: int, start: int) -> int:
        # From the question it's obvious we have Djikstra's algorithm
        graph = defaultdict(list)
        for v in times:
            source, target, weight = v[0], v[1], v[2]
            graph[source].append((target, weight))

        # Djikstra Recipe - begins here
        distance_map, parents_map = self.djikstra(n, graph, start)

        result = max(distance_map.values())
        if result != float('inf'):
            return result
        return -1