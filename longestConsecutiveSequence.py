# problem: https://leetcode.com/problems/longest-consecutive-sequence/
# Runtime: 320 ms, faster than 24.27% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 32.8 MB, less than 5.03% of Python3 online submissions for Longest Consecutive Sequence.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import deque
        elements = set(nums)
        visited = set()
        answer = 0
        for num in nums:
            if not num in visited:
                visited.add(num)
                queue = deque([num])
                tmp = 0
                while queue:
                    n = queue.popleft()
                    tmp += 1
                    if not n + 1 in visited and n + 1 in elements:
                        queue.append(n+1)
                        visited.add(n+1)
                    if not n - 1 in visited and n - 1 in elements:
                        queue.append(n-1)
                        visited.add(n-1)
                answer = max(tmp, answer)
        return answer
