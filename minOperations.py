# problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/submissions/
# Runtime: 1224 ms, faster than 50.00% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 36.6 MB, less than 50.00% of Python3 online submissions for Minimum Operations to Reduce X to Zero.

from typing import List


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:

        values = {}
        cur = 0
        lenArr = len(nums)
        for i in range(lenArr):
            cur += nums[i]
            values[cur] = i
        target = cur - x
        if target < 0:
            return -1
        answer = -1
        total = 0
        values[0] = -1
        for i in range(lenArr):
            total += nums[i]
            if (total-target) in values:
                if total == target:
                    print(i, total, target)
                answer = max(answer, i - values[total-target])
        return answer if answer == -1 else lenArr - answer
