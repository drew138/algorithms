# problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Runtime: 788 ms, faster than 38.93% of Python3 online submissions for Shortest Path in Binary Matrix.
# Memory Usage: 15.6 MB, less than 32.33% of Python3 online submissions for Shortest Path in Binary Matrix.

from typing import List


class Solution:
    connections = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def getConnection(self, i, j, n, m, grid):
        for x, y in Solution.connections:
            if 0 <= x + i < n and 0 <= y + j < m and not grid[x+i][y+j]:
                yield x + i, y + j

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n, m = len(grid), len(grid[0])
        visited = set()
        steps = 0
        queue = deque()
        if not grid[0][0]:
            queue.append((0, 0))
            visited.add((0, 0))
            steps += 1
        while queue:
            tmp = deque()
            while queue:
                el = queue.popleft()
                if el[0] == n - 1 and el[1] == m - 1:
                    return steps
                for item in self.getConnection(el[0], el[1], n, m, grid):
                    if not item in visited:
                        tmp.append(item)
                        visited.add(item)
            queue = tmp
            steps += 1
        return -1
