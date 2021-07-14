# problem: https://leetcode.com/problems/find-peak-element/
# Runtime: 48 ms, faster than 51.31% of Python3 online submissions for Find Peak Element.
# Memory Usage: 14.6 MB, less than 11.31% of Python3 online submissions for Find Peak Element.

from typing import List


class Solution:
    def isPeak(self, nums, i):
        isStart = i == 0
        isEnd = i == len(nums) - 1
        return (isStart and nums[0] > nums[1]) or (isEnd and nums[-1] > nums[-2]) or (nums[i-1] < nums[i] > nums[i+1])

    def isIncr(self, nums, i):
        isStart = i == 0
        isEnd = i == len(nums) - 1
        return (isStart and nums[0] < nums[1]) or (not isEnd and nums[i] < nums[i+1])

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i, j = 0, len(nums)

        while i < j:
            mid = ((j-i)//2) + i
            if self.isPeak(nums, mid):
                return mid
            if self.isIncr(nums, mid):
                i = mid + 1
            else:
                j = mid - 1
        return i
