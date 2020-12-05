# problem: https: // leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Runtime: 376 ms, faster than 27.66 % of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 22 MB, less than 65.36 % of Python3 online submissions for Find All Numbers Disappeared in an Array.

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []

        for index, num in enumerate(nums):
            num = abs(num)
            nums[num-1] = - abs(nums[num-1])

        for index, num in enumerate(nums):
            if num > 0:
                answer.append(index + 1)
        return answer
