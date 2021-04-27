# problem: https://leetcode.com/problems/power-of-three/
# Runtime: 64 ms, faster than 93.23% of Python3 online submissions for Power of Three.
# Memory Usage: 14.1 MB, less than 91.80% of Python3 online submissions for Power of Three.

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0
