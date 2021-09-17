# problem: https://leetcode.com/problems/spiral-matrix/
# Runtime: 32 ms, faster than 63.71% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.1 MB, less than 83.48% of Python3 online submissions for Spiral Matrix.

from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        answer = []
        i, j, dx, dy = 0, 0, 1, 0

        for _ in range(m * n):
            answer.append(matrix[i][j])
            matrix[i][j] = -101

            if dx == 1:

                if (j + dx) == n or matrix[i][j + dx] == -101:
                    dx = 0
                    dy = 1
                    i += dy
                    continue
                j += dx

            elif dx == -1:

                if j == 0 or matrix[i][j + dx] == -101:
                    dx = 0
                    dy = -1
                    i += dy
                    continue
                j += dx

            elif dy == 1:
                if (i + dy) == m or matrix[i + dy][j] == -101:
                    dx = -1
                    dy = 0
                    j += dx
                    continue
                i += dy

            elif dy == -1:
                if i == 0 or matrix[i + dy][j] == -101:
                    dx = 1
                    dy = 0
                    j += dx
                    continue
                i += dy
        return answer
