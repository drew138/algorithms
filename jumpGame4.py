# problem: https://leetcode.com/problems/jump-game-iv/
# Runtime: 544 ms, faster than 69.18% of Python3 online submissions for Jump Game IV.
# Memory Usage: 28.8 MB, less than 63.79% of Python3 online submissions for Jump Game IV.

from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import deque
        vals = {}
        for i, n in enumerate(arr):
            if n in vals:
                vals[n].append(i)
            else:
                vals[n] = [i]
        queue = deque()
        queue.append(0)
        steps = 0
        visited = set()
        while queue:
            layer = deque()
            while queue:
                el = queue.popleft()
                visited.add(el)
                if el == len(arr) - 1:
                    return steps
                if el + 1 < len(arr) and not (el + 1) in visited:
                    layer.append(el + 1)
                    visited.add(el + 1)
                if el - 1 >= 0 and not (el - 1) in visited:
                    layer.append(el - 1)
                    visited.add(el - 1)
                if arr[el] in vals:
                    for i in vals[arr[el]]:
                        if el != i and not i in visited:
                            layer.append(i)
                            visited.add(i)
                    del vals[arr[el]]
            steps += 1
            queue = layer

        return steps
