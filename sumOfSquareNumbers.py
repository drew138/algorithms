# problem: https://leetcode.com/problems/sum-of-square-numbers/
# Runtime: 351 ms, faster than 33.45% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 14.2 MB, less than 74.34% of Python3 online submissions for Sum of Square Numbers.

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = math.ceil(c ** (1 / 2))
        for i in range(n):
            if not ((c - (i ** 2)) ** (1/2) % 1):
                return True
        return c == 0
