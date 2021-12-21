# problem: https://leetcode.com/problems/power-of-four/
# Runtime: 32 ms, faster than 67.12% of Python3 online submissions for Power of Four.
# Memory Usage: 14.3 MB, less than 42.13% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        while n and n % 4 == 0:
            n /= 4
        return n == 1