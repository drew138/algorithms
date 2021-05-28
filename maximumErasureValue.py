# problem: https: // leetcode.com/problems/maximum-erasure-value/
# Runtime: 2756 ms, faster than 6.09% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 28.1 MB, less than 63.08% of Python3 online submissions for Maximum Erasure Value.
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import deque, defaultdict
        dp = {}
        start = 0
        end = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i] in dp:
                for j in range(start, dp[nums[i]]):
                    del dp[nums[j]]
                start = dp[nums[i]] + 1
            else:
                end = i
            dp[nums[i]] = i
            answer = max(answer, sum(nums[start:end + 1]))
        return answer
