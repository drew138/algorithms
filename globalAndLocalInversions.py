# problem: https: // leetcode.com/problems/global- and -local-inversions/
# Runtime: 316 ms, faster than 97.70 % of Python3 online submissions for Global and Local Inversions.
# Memory Usage: 15.1 MB, less than 44.06 % of Python3 online submissions for Global and Local Inversions.

from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(i - A[i]) > 1:
                return False
        return True
