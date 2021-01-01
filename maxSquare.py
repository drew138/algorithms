# problem: https://leetcode.com/problems/maximal-square/
# Runtime: 216 ms, faster than 29.86% of Python3 online submissions for Maximal Square.
# Memory Usage: 15.2 MB, less than 97.71% of Python3 online submissions for Maximal Square.

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxSide = 0
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] != "0":
                    down = 0 if i + 1 == m else int(matrix[i+1][j])
                    right = 0 if j + 1 == n else int(matrix[i][j + 1])
                    diagonal = 0 if j + 1 == n or i + \
                        1 == m else int(matrix[i + 1][j + 1])
                    matrix[i][j] = min(down, right, diagonal) + 1
                    maxSide = max(maxSide, matrix[i][j])
        return maxSide ** 2
