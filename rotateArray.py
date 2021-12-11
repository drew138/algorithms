# problem: https://leetcode.com/problems/rotate-array/
# Runtime: 224 ms, faster than 64.09% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.6 MB, less than 57.05% of Python3 online submissions for Rotate Array.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def aux(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
        if k > 0:
            aux(nums, 0, len(nums) - 1)
            aux(nums, 0, k - 1)
            aux(nums, k, len(nums) - 1)