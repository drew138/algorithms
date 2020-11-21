# problem: https://leetcode.com/problems/minimum-height-trees/submissions/
# Runtime: 240 ms, faster than 72.70% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 18.1 MB, less than 5.72% of Python3 online submissions for Minimum Height Trees.
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
            return []
        elif n == 1:
            return [0]

        nodes = [0] * n
        adj = [[] for _ in range(n)]
        for edge in edges:
            nodes[edge[0]] += 1
            nodes[edge[1]] += 1
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        queue = []
        for index, node in enumerate(nodes):
            if node == 1:
                queue.insert(0, index)
        while n > 2:
            size = len(queue)
            n -= size
            while size > 0:
                val = queue.pop(-1)
                for num in adj[val]:
                    nodes[num] -= 1
                    if nodes[num] == 1:
                        queue.insert(0, num)
                size -= 1
        return queue
