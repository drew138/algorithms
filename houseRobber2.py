# problem: https://leetcode.com/problems/house-robber-ii/
# Runtime: 46 ms, faster than 18.31% of Python3 online submissions for House Robber II.
# Memory Usage: 14.3 MB, less than 58.08% of Python3 online submissions for House Robber II.

from typing import List


class Solution:
    def aux(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] +
                          nums[i - 2], nums[i] + nums[i-3])
        return nums[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        return max(self.aux(nums[1:]), self.aux(nums[:-1]))
