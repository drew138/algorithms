# problem: https://leetcode.com/problems/sort-array-by-parity-ii/
# Runtime: 216 ms, faster than 54.85% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 16.2 MB, less than 73.54% of Python3 online submissions for Sort Array By Parity II.

from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 and (not nums[j] % 2):
                nums[i], nums[j] = nums[j], nums[i]
            if not nums[i] % 2:
                i += 2
            if nums[j] % 2:
                j += 2
        return nums
