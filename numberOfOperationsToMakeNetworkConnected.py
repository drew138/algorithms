# problem: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Runtime: 518 ms, faster than 67.57% of Python3 online submissions for Number of Operations to Make Network Connected.
# Memory Usage: 34.6 MB, less than 61.36% of Python3 online submissions for Number of Operations to Make Network Connected.

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        if len(connections) < n-1:
            return -1
        adj = defaultdict(list)
        visited = set()
        for start, end in connections:
            adj[start].append(end)
            adj[end].append(start)

        def get_sccs(n, adj):
            total = 0
            for i in range(n):
                if not i in visited:
                    total += 1
                    visited.add(i)
                    index = 0
                    queue = adj[i].copy()
                    while index < len(queue):
                        element = queue[index]
                        visited.add(element)
                        tmp = [x for x in adj[element] if not x in visited]
                        visited.update(tmp)
                        queue += tmp
                        index += 1
            return total

        number_of_sccs = get_sccs(n, adj)
        return number_of_sccs-1
