# problem: https: // leetcode.com/problems/majority-element/submissions/
# Runtime: 176 ms, faster than 19.30 % of Python3 online submissions for Majority Element.
# Memory Usage: 15.6 MB, less than 18.99 % of Python3 online submissions for Majority Element.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # from statistics import mode
        # return mode(nums)
        from collections import defaultdict
        count = defaultdict(int)
        mode = (len(nums) // 2) + 1
        for num in nums:
            count[num] += 1
            if count[num] >= mode:
                return num
