# problem: https://leetcode.com/problems/sort-the-matrix-diagonally/
# Runtime: 80 ms, faster than 89.62% of Python3 online submissions for Sort the Matrix Diagonally.
# Memory Usage: 14.8 MB, less than 24.99% of Python3 online submissions for Sort the Matrix Diagonally.

from typing import List


class Solution:
    def sortMatrix(self, i, j, mat):
        self.stack.sort(reverse=True)
        while i < len(mat) and j < len(mat[0]) and self.stack:
            num = self.stack.pop()
            mat[i][j] = num
            i += 1
            j += 1

    def getDiagonal(self, i, j, mat):
        x, y = i, j
        while i < len(mat) and j < len(mat[0]):
            self.stack.append(mat[i][j])
            i += 1
            j += 1
        self.sortMatrix(x, y, mat)

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        self.stack = []
        for i in range(m - 1, -1, -1):
            self.getDiagonal(i, 0, mat)

        for i in range(1, n):
            self.getDiagonal(0, i, mat)
        return mat
