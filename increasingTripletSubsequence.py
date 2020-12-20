# problem: https://leetcode.com/problems/increasing-triplet-subsequence/
# Runtime: 56 ms, faster than 46.89% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 14.9 MB, less than 7.12% of Python3 online submissions for Increasing Triplet Subsequence.

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        from collections import deque
        stack = deque()
        maxLen = 0
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)
            maxLen = max(maxLen, len(stack))
        incr = 0
        cur = nums[0]
        for num in nums:
            if num > cur:
                incr += 1
                cur = num
        return (maxLen >= 3) or (incr >= 2)
