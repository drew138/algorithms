# problem: https://leetcode.com/problems/power-of-two/
# Runtime: 32 ms, faster than 69.55% of Python3 online submissions for Power of Two.
# Memory Usage: 14.3 MB, less than 7.09% of Python3 online submissions for Power of Two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        total = 0
        while n:
            total += n & 1
            n >>= 1
        return total == 1