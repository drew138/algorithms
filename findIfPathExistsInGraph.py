# problem: https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# Runtime
# 1850 ms
# Beats
# 92.57%
# Memory
# 106.4 MB
# Beats
# 48.51%


from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        queue = [source]
        visited = [False] * n
        adj = defaultdict(list)

        visited[source] = True
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        for node in queue:
            for connection in adj[node]:
                if connection == destination:
                    return True
                if not visited[connection]:
                    visited[connection] = True
                    queue.append(connection)
        return False
