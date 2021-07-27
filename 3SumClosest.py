# problem: https://leetcode.com/problems/3sum-closest/
# Runtime: 356 ms, faster than 16.59% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.4 MB, less than 42.28% of Python3 online submissions for 3Sum Closest.

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        answer = float("inf")
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                answer = tmp if abs(
                    target-tmp) < abs(target-answer) else answer
                if tmp < target:
                    j += 1
                else:
                    k -= 1
        return answer
