# problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# Runtime: 505 ms, faster than 58.78% of Python3 online submissions for Jump Game.
# Memory Usage: 15.5 MB, less than 11.89% of Python3 online submissions for Jump Game.


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_reach = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= min_reach:
                min_reach = i
        return min_reach == 0
