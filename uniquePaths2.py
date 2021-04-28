# problem: https: // leetcode.com/problems/unique-paths-ii/
# Runtime: 40 ms, faster than 78.35% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14 MB, less than 98.99% of Python3 online submissions for Unique Paths II.

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        obstacleGrid[0][0] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and obstacleGrid[i-1][j] <= 0:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j > 0 and obstacleGrid[i][j-1] <= 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return abs(obstacleGrid[-1][-1])
