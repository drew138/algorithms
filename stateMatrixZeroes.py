# problem: https://leetcode.com/problems/set-matrix-zeroes/
# Runtime: 128 ms, faster than 71.68% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.1 MB, less than 74.68% of Python3 online submissions for Set Matrix Zeroes.

from typing import List


class Solution:

    def convertRow(self, i, matrix):

        for j in range(len(matrix[i])):
            if matrix[i][j]:
                matrix[i][j] = " "

    def convertColumn(self, j, matrix):

        for i in range(len(matrix)):
            if matrix[i][j]:
                matrix[i][j] = " "

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    self.convertRow(i, matrix)
                    self.convertColumn(j, matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == " ":
                    matrix[i][j] = 0
        return matrix
