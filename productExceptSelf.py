# problem: https://leetcode.com/problems/product-of-array-except-self/submissions/
# Runtime: 220 ms, faster than 65.12% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21 MB, less than 50.74% of Python3 online submissions for Product of Array Except Self.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenArr = len(nums)
        answer = [1] * lenArr
        prev = 1
        for i in range(lenArr):
            answer[i] = prev
            prev = nums[i] * prev
        prev = 1
        while lenArr:
            answer[lenArr - 1] = prev * answer[lenArr - 1]
            prev = prev * nums[lenArr - 1]

            lenArr -= 1
        return answer
