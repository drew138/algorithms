# problem: https://leetcode.com/problems/squares-of-a-sorted-array/
# Runtime: 232 ms, faster than 38.77% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16 MB, less than 77.54% of Python3 online submissions for Squares of a Sorted Array.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                answer.append(nums[i] ** 2)
                i += 1
            else:
                answer.append(nums[j] ** 2)
                j -= 1
        return reversed(answer)
