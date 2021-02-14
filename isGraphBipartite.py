# problem: https://leetcode.com/problems/is-graph-bipartite/
# Runtime: 168 ms, faster than 91.07% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 14.7 MB, less than 54.88% of Python3 online submissions for Is Graph Bipartite?.

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for i in range(len(graph)):
            if (colors[i] == 0) and (not self.isValid(graph, colors, 1, i)):
                return False
        return True

    def isValid(self, nodes, colors, color, node):
        if colors[node] != 0:
            return colors[node] == color
        colors[node] = color
        for i in nodes[node]:
            if not self.isValid(nodes, colors, -color, i):
                return False
        return True
