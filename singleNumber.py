# problem: https://leetcode.com/problems/single-number/
# Runtime: 128 ms, faster than 85.62% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 60.21% of Python3 online submissions for Single Number.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = nums[0]
        for num in nums[1:]:
            tmp ^= num
        return tmp
