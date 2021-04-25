# problem: https://leetcode.com/problems/critical-connections-in-a-network/
# Runtime: 2272 ms, faster than 72.41% of Python3 online submissions for Critical Connections in a Network.
# Memory Usage: 98 MB, less than 34.96% of Python3 online submissions for Critical Connections in a Network.

from typing import List


class Solution:

    def dfs(self, node, adj, visited, disc, low, answer, prev):

        disc[node] = self.time
        low[node] = self.time
        self.time += 1
        for child in adj[node]:
            if not child in visited:
                visited.add(child)
                self.dfs(child, adj, visited, disc, low, answer, node)
                low[node] = min(low[node], low[child])
            elif child != prev:
                low[node] = min(low[node], disc[child])
            if low[child] > disc[node]:
                answer.add((child, node))

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        visited = set()
        adj = defaultdict(list)
        self.time = 0
        disc = {}
        low = {}
        answer = set()
        for con in connections:
            a, b = con
            adj[a].append(b)
            adj[b].append(a)
        self.dfs(0, adj, visited, disc, low, answer, -1)
        return list(answer)
