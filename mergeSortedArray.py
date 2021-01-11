# problem: https://leetcode.com/problems/merge-sorted-array/
# Runtime: 24 ms, faster than 99.51% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.4 MB, less than 29.25% of Python3 online submissions for Merge Sorted Array.

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer = [None] * (m + n)
        i = j = k = 0
        while i < m or j < n:
            first = nums1[i] if i < m else float("inf")
            second = nums2[j] if j < n else float("inf")
            if first > second:
                answer[k] = nums2[j]
                j += 1
            else:
                answer[k] = nums1[i]
                i += 1
            k += 1
        for i, num in enumerate(answer):
            nums1[i] = num
