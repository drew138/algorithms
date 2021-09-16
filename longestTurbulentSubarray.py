# problem: https://leetcode.com/problems/longest-turbulent-subarray/
# Runtime: 604 ms, faster than 26.89% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 18.9 MB, less than 14.36% of Python3 online submissions for Longest Turbulent Subarray.


from typing import List
from collections import deque


class Solution:
    def aux(self, queue, num):
        n = len(queue)
        if n == 1 and num != queue[0]:
            queue.append(num)
        elif n >= 1 and num == queue[n-1]:
            queue = deque([num])
        elif n >= 2 and (queue[n-2] > queue[n-1] > num or queue[n-2] < queue[n-1] < num):
            tmp = queue.pop()
            queue = deque([tmp, num])
        else:
            queue.append(num)
        return len(queue), queue

    def maxTurbulenceSize(self, arr: List[int]) -> int:

        q = deque()

        answer = 0
        for i, num in enumerate(arr):
            l, q = self.aux(q, num)
            answer = max(answer, l)
        return answer
