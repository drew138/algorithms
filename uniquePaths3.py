# problem: https://leetcode.com/problems/unique-paths-iii/
# Runtime: 60 ms, faster than 73.90% of Python3 online submissions for Unique Paths III.
# Memory Usage: 14.3 MB, less than 46.77% of Python3 online submissions for Unique Paths III.


from typing import List


class Solution:

    dirs = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def checkGrid(self, grid):
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    return False
        return True

    def traverse(self, grid, x, y):
        if (x, y) == self.end:
            return 1 if self.checkGrid(grid) else 0

        total = 0
        for a, b in self.dirs:
            c1 = 0 <= x + a < self.m
            c2 = 0 <= y + b < self.n
            if c1 and c2 and grid[x + a][y + b] == 0:
                grid[x + a][y + b] = 1
                total += self.traverse(grid, x + a, y + b)
                grid[x + a][y + b] = 0
        return total

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start, self.end = None, None
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    self.end = (i, j)
                    grid[i][j] = 0
        return self.traverse(grid, start[0], start[1])
