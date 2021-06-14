# problem: https://leetcode.com/problems/min-cost-climbing-stairs/
# Runtime: 56 ms, faster than 69.27% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.5 MB, less than 39.46% of Python3 online submissions for Min Cost Climbing Stairs.

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        for i in range(2, len(cost)):
            cost[i] = min(cost[i] + cost[i-1], cost[i] + cost[i-2])
        return min(cost[-1], cost[-2])
