# problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime: 60 ms, faster than 88.90% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.2 MB, less than 46.58% of Python3 online submissions for Kth Largest Element in an Array.

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
