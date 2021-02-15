# problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Runtime: 112 ms, faster than 48.13% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 15.1 MB, less than 16.13% of Python3 online submissions for The K Weakest Rows in a Matrix.

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        from sortedcontainers import SortedList
        l = SortedList()
        for i, row in enumerate(mat):
            l.add((sum(row), i))
        answer = []
        while k:
            _, b = l.pop(0)
            answer.append(b)
            k -= 1
        return answer
