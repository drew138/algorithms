# problem: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Runtime: 1244 ms, faster than 15.57% of Python3 online submissions for Arithmetic Slices II - Subsequence.
# Memory Usage: 186.6 MB, less than 10.38% of Python3 online submissions for Arithmetic Slices II - Subsequence.

from typing import List


class Solution:

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        from collections import defaultdict

        answer = 0
        dp = defaultdict(int)

        for i in range(1, len(nums)):
            for j in range(i):
                dif = nums[i] - nums[j]
                answer += dp[(j, dif)]
                dp[(i, dif)] += dp[(j, dif)] + 1

        return answer
