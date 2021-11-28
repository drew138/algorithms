# problem: https://leetcode.com/problems/all-paths-from-source-to-target/
# Runtime: 100 ms, faster than 74.93% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.9 MB, less than 19.64% of Python3 online submissions for All Paths From Source to Target.

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque
        n = len(graph)
        queue = deque([[0]])
        sol = []
        while queue:
            path = queue.popleft()
            if path[-1] == n - 1:
                sol.append(path)
            else:
                for node in graph[path[-1]]:
                    copy = [*path, node]
                    queue.append(copy)
        return sol
