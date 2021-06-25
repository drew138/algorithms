# problem: https://leetcode.com/problems/redundant-connection/
# Runtime: 44 ms, faster than 99.33% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.9 MB, less than 66.44% of Python3 online submissions for Redundant Connection.

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        for edge in edges:
            if self.find(edge[0], parents) == self.find(edge[1], parents):
                return edge
            self.union(edge[0], edge[1], parents)
        return None

    def find(self, node, parents):
        while parents[node] != node:
            node = parents[node]
        return node

    def union(self, i, j, parents):
        ir = self.find(i, parents)
        jr = self.find(j, parents)
        if ir != jr:
            parents[jr] = ir
