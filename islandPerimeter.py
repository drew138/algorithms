# problem: https://leetcode.com/problems/island-perimeter/
# Runtime: 840 ms, faster than 16.50% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14.7 MB, less than 61.43% of Python3 online submissions for Island Perimeter.

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        answer += not ((0 <= i + x < n and 0 <=
                                        j + y < m) and grid[i+x][j+y])
        return answer
