# problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Runtime: 50 ms, faster than 14.68% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.7 MB, less than 29.49% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = ((j - i) // 2) + i
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]
