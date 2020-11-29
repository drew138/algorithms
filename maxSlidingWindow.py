# problem: https://leetcode.com/problems/sliding-window-maximum/submissions/
# Runtime: 1312 ms, faster than 95.87% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 29.6 MB, less than 89.06% of Python3 online submissions for Sliding Window Maximum.

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        answer = []
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        answer.append(nums[queue[0]])
        if len(queue) == k:
            queue.popleft()

        for i in range(k, len(nums)):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if (i - queue[0]) == k:
                queue.popleft()
            answer.append(nums[queue[0]])
        return answer
