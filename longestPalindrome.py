# problem: https://leetcode.com/problems/longest-palindrome/description/
# Runtime
# 37 ms
# Beats
# 82.6%
# Memory
# 13.8 MB
# Beats
# 65.59%

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        ans = 0
        has_odd = False
        for val in counter.values():
            if val & 1:
                has_odd = True
                val -= 1
            ans += val
        ans += has_odd
        return ans
