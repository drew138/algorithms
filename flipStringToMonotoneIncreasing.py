# problem: https: // leetcode.com/problems/flip-string-to-monotone-increasing/
# Runtime: 248 ms, faster than 9.30 % of Python3 online submissions for Flip String to Monotone Increasing.
# Memory Usage: 19.7 MB, less than 6.98 % of Python3 online submissions for Flip String to Monotone Increasing.

from itertools import accumulate


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        acc, n = [0] + list(accumulate(map(int, s))), len(s)
        return min(2*acc[i] + n - i - acc[-1] for i in range(n+1))
