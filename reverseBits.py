# problem: https://leetcode.com/problems/reverse-bits/submissions/
# Runtime: 24 ms, faster than 96.17% of Python3 online submissions for Reverse Bits.
# Memory Usage: 14.2 MB, less than 24.55% of Python3 online submissions for Reverse Bits.

class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        iters = 32
        while iters:
            bit = n % 2
            answer <<= 1
            n >>= 1
            answer |= bit
            iters -= 1
        return answer
