# problem: https://leetcode.com/problems/shuffle-the-array/
# Runtime: 56 ms, faster than 83.75% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.3 MB, less than 59.99% of Python3 online submissions for Shuffle the Array.

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = len(nums) * [None]
        for i in range(len(nums)//2):
            answer[2 * i] = nums[i]
        j = 0
        for i in range(len(nums)//2, len(nums)):
            answer[(2 * j) + 1] = nums[i]
            j += 1

        return answer
