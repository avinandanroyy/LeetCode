from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                # The leaf has exactly one neighbor
                neighbor = adj[leaf].pop()
                # Remove the edge from the neighbor back to the leaf
                adj[neighbor].remove(leaf)
                
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        return list(leaves)

sol = Solution()
print(sol.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))