# problem: https://leetcode.com/problems/valid-triangle-number/
# Runtime: 1128 ms, faster than 69.97% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.5 MB, less than 30.98% of Python3 online submissions for Valid Triangle Number.

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        answer = 0
        for i in range(2, n):
            j, k = 0, i-1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    answer += k - j
                    k -= 1
                else:
                    j += 1
        return answer
