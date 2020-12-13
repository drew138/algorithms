# problem: https://leetcode.com/problems/triangle/
# Runtime: 56 ms, faster than 79.12% of Python3 online submissions for Triangle.
# Memory Usage: 14.9 MB, less than 40.45% of Python3 online submissions for Triangle.

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == (len(triangle[i]) - 1):
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
