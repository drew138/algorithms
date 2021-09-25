# problem: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Runtime: 916 ms, faster than 23.65% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
# Memory Usage: 22.8 MB, less than 8.52% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.

from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        from collections import deque
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = deque([(0, 0, k, 0)])
        while queue:
            x, y, z, l = queue.popleft()
            if (x, y) == (n - 1, m - 1):
                return l
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < n and 0 <= y + j < m and z-grid[x+i][y+j] >= 0:
                    new = (x+i, y+j, z-grid[x+i][y+j])
                    if not new in visited:
                        visited.add(new)
                        queue.append(new + (l+1,))
        return -1
