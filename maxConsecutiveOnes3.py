# problem: https://leetcode.com/problems/max-consecutive-ones-iii/
# Runtime: 628 ms, faster than 60.14% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.8 MB, less than 68.72% of Python3 online submissions for Max Consecutive Ones III.

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        from collections import deque
        tmp = 0
        window = deque()
        answer = 0
        for num in nums:

            if tmp == k and not num:
                while window and window[0]:
                    window.popleft()
                if window and not window[0]:
                    window.popleft()
                    tmp -= 1
            if tmp < k or num:
                window.append(num)
                if not num:
                    tmp += 1
            answer = max(answer, len(window))
        return answer
