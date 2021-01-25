# problem: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Runtime: 560 ms, faster than 71.14% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
# Memory Usage: 16.8 MB, less than 97.76% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = None
        for i in range(len(nums)):
            if index != None and nums[i] and i - index - 1 < k:

                return False
            if nums[i]:
                index = i
        return True
