# problem: https://leetcode.com/problems/minimum-absolute-difference/
# Runtime: 324 ms, faster than 89.20% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 28.2 MB, less than 60.76% of Python3 online submissions for Minimum Absolute Difference.

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        from collections import defaultdict
        pairs = defaultdict(list)
        n = len(arr)
        m = float("inf")
        arr.sort()
        for i in range(1, n):
            prev = arr[i - 1]
            cur = arr[i]
            dif = cur - prev
            if m >= dif:
                pairs[dif].append([prev, cur])
                m = dif
        return pairs[m]