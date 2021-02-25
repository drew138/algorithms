# problem: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Runtime: 212 ms, faster than 59.02% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 15.4 MB, less than 70.70% of Python3 online submissions for Shortest Unsorted Continuous Subarray.

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        cp = nums.copy()
        cp.sort()
        start = float("inf")
        end = -float("inf")
        isSorted = True
        for i in range(len(nums)):
            if nums[i] != cp[i]:
                start = min(start, i)
                end = max(start, i)
                isSorted = False
        if isSorted:
            return 0
        return end - start + 1
