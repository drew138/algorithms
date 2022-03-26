# problem: https://leetcode.com/problems/powx-n/
# Runtime: 24 ms, faster than 98.94% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.8 MB, less than 98.13% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        sol = 1
        while n:
            if n & 1:
                sol *= x
            x *= x
            n >>= 1
        return sol
    