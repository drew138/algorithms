# problem: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Runtime: 312 ms, faster than 98.71% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
# Memory Usage: 15.7 MB, less than 55.95% of Python3 online submissions for Number of Subarrays with Bounded Maximum.

from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        answer = 0
        l, r = -1, -1
        for i in range(len(nums)):
            if nums[i] > right:
                r = i
            if nums[i] >= left:
                l = i
            answer += l - r
        return answer
