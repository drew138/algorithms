# problem: https://leetcode.com/problems/unique-paths-ii/
# Runtime: 32 ms, faster than 98.34% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.4 MB, less than 23.49% of Python3 online submissions for Unique Paths II.

from typing import List


class Solution:
    def getCellVal(self, x, y):
        ver = x == 0 or self.obstacleGrid[x-1][y] > 0
        hor = y == 0 or self.obstacleGrid[x][y-1] > 0
        if ver and not hor:
            return self.obstacleGrid[x][y-1]
        elif not ver and hor:
            return self.obstacleGrid[x-1][y]
        elif not ver and not hor:
            return self.obstacleGrid[x-1][y] + self.obstacleGrid[x][y-1]
        else:
            return self.obstacleGrid[x][y]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.numRows = len(obstacleGrid)
        self.numCols = len(obstacleGrid[0])
        self.obstacleGrid = obstacleGrid
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] <= 0:
                    obstacleGrid[i][j] = self.getCellVal(i, j)
        return abs(obstacleGrid[-1][-1]) if obstacleGrid[-1][-1] < 0 else 0
