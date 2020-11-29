# problem: https: // leetcode.com/problems/jump-game-iii/
# Runtime: 212 ms, faster than 81.49% of Python3 online submissions for Jump Game III.
# Memory Usage: 20.7 MB, less than 52.08% of Python3 online submissions for Jump Game III.

from typing import List


class Solution:

    def isValid(self, index):
        return index >= 0 and index < self.lenArr and not index in self.visited

    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque

        queue = deque()
        self.lenArr = len(arr)
        self.visited = set()
        self.visited.add(start)
        queue.append(start)
        while queue:
            index = queue.pop()
            if arr[index] == 0:
                return True
            if self.isValid(index + arr[index]):
                queue.appendleft(index + arr[index])
                self.visited.add(index + arr[index])
            if self.isValid(index - arr[index]):
                queue.appendleft(index - arr[index])
                self.visited.add(index - arr[index])
        return False
