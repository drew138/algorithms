# problem: https://leetcode.com/problems/reshape-the-matrix/
# Runtime: 88 ms, faster than 65.98% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 15.2 MB, less than 20.69% of Python3 online submissions for Reshape the Matrix.

from typing import List


class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if n * m != r * c:
            return mat
        gen = (mat[i][j] for i in range(n) for j in range(m))
        return [[gen.__next__() for _ in range(c)] for _ in range(r)]
