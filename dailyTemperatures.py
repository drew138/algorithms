# problem: https://leetcode.com/problems/daily-temperatures/
# Runtime: 500 ms, faster than 80.55% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 18.5 MB, less than 76.70% of Python3 online submissions for Daily Temperatures.
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append((T[i], i))
        return answer
