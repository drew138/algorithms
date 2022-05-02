# problem: https://leetcode.com/problems/sort-array-by-parity/
# Runtime: 88 ms, faster than 72.64% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0 , n - 1
        while l < r:
            if nums[l] & 1:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return nums
