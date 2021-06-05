# problem: https://leetcode.com/problems/open-the-lock/
# Runtime: 704 ms, faster than 42.76% of Python3 online submissions for Open the Lock.
# Memory Usage: 15.6 MB, less than 58.15% of Python3 online submissions for Open the Lock

from typing import List


class Solution:
    def getConnections(self, num):
        for i in range(len(num)):
            for h in (-1, 1):
                yield num[:i] + str((int(num[i:i+1])+h) % 10) + num[i+1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        visited = set(deadends)
        if "0000" in visited:
            return -1
        queue = deque()
        queue.append(("0000", 0))
        answer = -1
        while queue:
            num, steps = queue.popleft()
            if num == target:
                answer = steps
                break
            for connection in self.getConnections(num):
                if not connection in visited:
                    visited.add(connection)
                    queue.append((connection, steps + 1))
        return answer
