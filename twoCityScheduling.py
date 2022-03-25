# problem: https://leetcode.com/problems/two-city-scheduling/
# Runtime: 60 ms, faster than 49.03% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.8 MB, less than 82.59% of Python3 online submissions for Two City Scheduling.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0] - x[1]))
        n = len(costs) // 2
        return sum([x[0] for x in costs[:n]]) + sum([x[1] for x in costs[n:]])

