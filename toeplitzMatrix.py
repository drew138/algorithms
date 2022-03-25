# problem: https://leetcode.com/problems/toeplitz-matrix/
# Runtime: 88 ms, faster than 91.51% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 14 MB, less than 14.51% of Python3 online submissions for Toeplitz Matrix.

from typing import List

class Solution:
    
    def check_diagonal(self, n, m, matrix, i, j):
        start = matrix[i][j]
        while i < n and j < m and matrix[i][j] == start:
            i += 1
            j += 1
        return i == n or j == m
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            if not self.check_diagonal(n, m, matrix, i, 0):
                return False
        
        for i in range(1, m):
            if not self.check_diagonal(n, m, matrix, 0, i):
                return False
        return True
