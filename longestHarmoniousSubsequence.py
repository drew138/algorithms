# problem: https://leetcode.com/problems/longest-harmonious-subsequence/
# Runtime: 400 ms, faster than 15.70% of Python3 online submissions for Longest Harmonious Subsequence.
# Memory Usage: 16 MB, less than 66.31% of Python3 online submissions for Longest Harmonious Subsequence.

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        m = 0
        for key in counter.keys():
            if counter[key+1]:
                m = max(m, counter[key] + counter[key+1])
        return m
