# problem: https://leetcode.com/problems/array-nesting/submissions/
# Runtime: 136 ms, faster than 37.50% of Python3 online submissions for Array Nesting.
# Memory Usage: 19.2 MB, less than 27.63% of Python3 online submissions for Array Nesting.

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        from collections import deque

        visited = set()
        answer = 0
        for i in range(len(nums)):
            queue = deque()
            queue.append(i)
            tmp = 0
            while queue:
                n = queue.popleft()
                if n in visited:
                    break
                visited.add(n)
                tmp += 1
                queue.append(nums[n])
            answer = max(answer, tmp)
        return answer
