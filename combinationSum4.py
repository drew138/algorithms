# problem: https://leetcode.com/problems/combination-sum-iv/
# Runtime: 44 ms, faster than 46.15% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.3 MB, less than 70.13% of Python3 online submissions for Combination Sum IV.

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (max(nums + [target]) + 1)
        nums.sort()
        for num in nums:
            dp[num] = 1
            if num > target:
                break
        for i in range(target+1):
            for num in nums:
                if i + num < len(dp):
                    dp[num+i] += dp[i]
        return dp[target]
