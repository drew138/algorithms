# problem: https://leetcode.com/problems/find-the-town-judge/
# Runtime: 749 ms, faster than 41.00% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.9 MB, less than 65.18% of Python3 online submissions for Find the Town Judge.

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [False] * n
        is_trusted = [0] * n
        for a, b in trust:
            trusts[a - 1] = True
            is_trusted[b - 1] += 1
        for i in range(n):
            if (not trusts[i]) and (is_trusted[i] == n - 1):
                return i + 1
        return -1