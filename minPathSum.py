# problem: https: // leetcode.com/problems/minimum-path-sum/submissions/
# Runtime: 92 ms, faster than 82.88 % of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 15.7 MB, less than 22.86 % of Python3 online submissions for Minimum Path Sum.

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        for i in range(1, width):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, height):
            for j in range(width):
                if j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
