# problem: https://leetcode.com/problems/range-sum-query-2d-immutable/
# Runtime: 104 ms, faster than 88.40% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 17.2 MB, less than 69.16% of Python3 online submissions for Range Sum Query 2D - Immutable.

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j > 0:
                    self.matrix[i][j] += self.matrix[i][j-1]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > 0:
                    self.matrix[i][j] += self.matrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row = self.matrix[row2][col1-1] if col1 > 0 else 0
        col = self.matrix[row1-1][col2] if row1 > 0 else 0
        tmp = self.matrix[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        return self.matrix[row2][col2] - row - col + tmp


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
