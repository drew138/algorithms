# problem: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
# Runtime: 688 ms, faster than 47.17% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
# Memory Usage: 32.5 MB, less than 13.04% of Python3 online submissions for Check If Array Pairs Are Divisible by k.

from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict
        m = defaultdict(int)
        visited = set()
        for i in range(len(arr)):
            m[arr[i] % k] += 1
        if m[0] % 2 == 1:
            return False
        for i in range(1, k):
            if m[i] != m[k - i]:
                return False
        return True
