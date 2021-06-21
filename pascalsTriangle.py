# problem: https://leetcode.com/problems/pascals-triangle/
# Runtime: 32 ms, faster than 61.41% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 14.3 MB, less than 22.00% of Python3 online submissions for Pascal's Triangle.

from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for i in range(numRows - 1):
            prevRow = answer[-1]
            answer.append([1] + [prevRow[i] + prevRow[i+1]
                                 for i in range(len(prevRow) - 1)] + [1])
        return answer
