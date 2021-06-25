# https://leetcode.com/problems/out-of-boundary-paths/
# Runtime: 132 ms, faster than 69.17% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 23.5 MB, less than 5.18% of Python3 online submissions for Out of Boundary Paths.


from functools import lru_cache


class Solution:
    DIRS = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    @lru_cache(None)
    def dfs(self, x, y, moves):
        if 0 > x or 0 > y or x == self.m or y == self.n:
            return 1
        if not moves:
            return 0
        total = 0
        for a, b in self.DIRS:
            total += self.dfs(x + a, y + b, moves - 1)
        return total % (10**9 + 7)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        return self.dfs(startRow, startColumn, maxMove)
