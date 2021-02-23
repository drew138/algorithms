# problem: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Runtime: 160 ms, faster than 84.41% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.5 MB, less than 68.22% of Python3 online submissions for Search a 2D Matrix II.

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = 0, len(matrix[0]) - 1
        while m >= 0 and n < len(matrix):
            val = matrix[n][m]
            if val == target:
                return True
            elif val < target:
                n += 1
            else:
                m -= 1
        return False
