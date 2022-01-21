# problem: https://leetcode.com/problems/gas-station/
# Runtime: 690 ms, faster than 28.31% of Python3 online submissions for Gas Station.
# Memory Usage: 19.1 MB, less than 9.60% of Python3 online submissions for Gas Station.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        u = [gas[i] - cost[i] for i in range(n)]
        sol = 0
        cur = 0
        total = 0
        for i, val in enumerate(u):
            cur += val
            if cur < 0:
                total += cur
                cur = 0
                sol = i + 1
        total += cur
        return sol if total >= 0 else -1
