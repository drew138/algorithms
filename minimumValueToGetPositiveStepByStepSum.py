# problem: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Runtime: 32 ms, faster than 73.73% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.1 MB, less than 92.09% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        m = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            m = min(m, nums[i])

        return abs(m) + 1 if m <= 0 else 1
