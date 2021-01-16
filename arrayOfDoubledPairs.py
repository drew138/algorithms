# problem: https://leetcode.com/problems/array-of-doubled-pairs/
# Runtime: 576 ms, faster than 88.17% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.6 MB, less than 57.71% of Python3 online submissions for Array of Doubled Pairs.

from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        from collections import Counter
        count = Counter(A)
        keys = list(count.keys())
        keys.sort()
        for key in keys:
            if count[key]:
                if count[2 * key] >= count[key]:
                    count[2 * key] -= count[key]
                    count[key] = 0
                elif count[(1/2) * key] >= count[key]:
                    count[(1/2) * key] -= count[key]
                    count[key] = 0
                else:
                    return False

        return True


class Solution:
    def getConnections(self, element):
        connections = []
        for i in range(4):
            el = [s for s in element]
            el[i] = str(int(el[i]) + 1) if el[i] != "9" else "0"
            connections.append("".join(el))
            el[i] = str(int(el[i]) - 1) if el[i] != "1" else "0"
            connections.append("".join(el))
        return connections

    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        deadends = set(deadends)
        queue = deque()
        queue.append("0000")
        layer = 0
        while queue:
            tmp = deque()
            while queue:
                element = queue.popleft()
                if element == target:
                    return layer
                connections = self.getConnections(element)
                for connection in connections:
                    if not connection in deadends:
                        tmp.append(connection)
            layer += 1
            queue = tmp
        return -1
