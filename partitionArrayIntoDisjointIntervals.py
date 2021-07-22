# problem: https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Runtime: 204 ms, faster than 56.46% of Python3 online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 18.3 MB, less than 68.12% of Python3 online submissions for Partition Array into Disjoint Intervals.

from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        forward = []
        backward = []
        for num in nums:
            if not forward:
                forward.append(num)
                continue
            forward.append(max(num, forward[-1]))
        for num in nums[::-1]:
            if not backward:
                backward.append(num)
                continue
            backward.append(min(num, backward[-1]))
        backward.reverse()
        for i in range(len(forward) - 1):
            if backward[i + 1] >= forward[i]:
                return i + 1
        return len(forward) - 1
