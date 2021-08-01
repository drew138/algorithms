# problem: https://leetcode.com/problems/trapping-rain-water/
# Runtime: 56 ms, faster than 61.34% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.2 MB, less than 16.73% of Python3 online submissions for Trapping Rain Water.


from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        forward = [heights[0]]
        backward = [heights[-1]]
        for height in heights[1:]:
            forward.append(max(forward[-1], height))
        for height in heights[::-1][1:]:
            backward.append(max(backward[-1], height))
        answer = 0
        backward.reverse()
        for i in range(len(heights)):
            answer += min(forward[i], backward[i]) - heights[i]
        return answer
