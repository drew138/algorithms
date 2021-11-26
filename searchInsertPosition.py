# problem: https://leetcode.com/problems/search-insert-position/
# Runtime: 68 ms, faster than 18.74% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15 MB, less than 56.94% of Python3 online submissions for Search Insert Position.

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:

            mid = ((r - l) // 2) + l
            if nums[mid] < target:
                mid += 1
                l = mid
            else:
                r = mid

        return mid
