# problem: https://leetcode.com/problems/counting-bits/
# Runtime: 215 ms, faster than 20.05% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 87.66% of Python3 online submissions for Counting Bits.

from typing import List

class Solution:
    def numBits(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        sol = [0] * (n + 1)
        for i in range(n + 1):
            sol[i] = self.numBits(i)
        return sol