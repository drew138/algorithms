# problem: https://leetcode.com/problems/arithmetic-slices/
# Runtime: 40 ms, faster than 48.59% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.5 MB, less than 51.21% of Python3 online submissions for Arithmetic Slices.

from typing import List


class Solution:
    def numSlices(self, i, j):
        if j - i < 3:
            return 0
        total = 0
        for x in range(3, j - i + 1):
            total += (j-i) - x + 1
        return total

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        i, j = 0, 1
        dif = A[j] - A[i]
        answer = 0
        while j < len(A):
            while j < len(A) and A[j] - A[j-1] == dif:
                j += 1
            answer += self.numSlices(i, j)
            if j == len(A):
                break
            i = j - 1
            dif = A[j] - A[i]
        return answer
