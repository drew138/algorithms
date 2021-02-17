# problem: https://leetcode.com/problems/container-with-most-water/
# Runtime: 168 ms, faster than 75.03% of Python3 online submissions for Container With Most Water.
# Memory Usage: 16.8 MB, less than 20.63% of Python3 online submissions for Container With Most Water.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        answer = 0
        while i < j:
            answer = max((j - i) * min(height[i], height[j]), answer)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return answer
