# problem: https://leetcode.com/problems/house-robber/
# Runtime: 32 ms, faster than 69.26% of Python3 online submissions for House Robber.
# Memory Usage: 14.1 MB, less than 79.02% of Python3 online submissions for House Robber.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] +
                          nums[i - 2], nums[i] + nums[i-3])
        return nums[-1]
