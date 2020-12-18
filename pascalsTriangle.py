# problem: https://leetcode.com/problems/pascals-triangle/
# Runtime: 32 ms, faster than 54.00% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 14.2 MB, less than 49.45% of Python3 online submissions for Pascal's Triangle.

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[None for _ in range(n + 1)] for n in range(numRows)]
        for l in answer:
            l[0] = 1
            l[-1] = 1
        for i in range(1, numRows):
            for j in range(1, len(answer[i]) - 1):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer
