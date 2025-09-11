from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value

        def bfs_search(start_node, end_node):
            if start_node not in graph or end_node not in graph:
                return -1.0

            queue = collections.deque([(start_node, 1.0)])
            visited = {start_node}

            while queue:
                current_node, current_product = queue.popleft()

                if current_node == end_node:
                    return current_product

                for neighbor, weight in graph[current_node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_product * weight))
            return -1.0

        results = []
        for query in queries:
            start, end = query
            results.append(bfs_search(start, end))

        return results

sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))