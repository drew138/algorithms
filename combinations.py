# problem: https://leetcode.com/problems/combinations/
# Runtime: 88 ms, faster than 87.75% of Python3 online submissions for Combinations.
# Memory Usage: 15.6 MB, less than 50.59% of Python3 online submissions for Combinations.

from typing import List


class Solution:
    def traverse(self, i, L, arr):
        if not L:
            self.answer.append(arr.copy())
            return
        for j in range(i + 1, self.N - L + 2):
            arr.append(j)
            self.traverse(j, L - 1, arr)
            arr.pop()

    def combine(self, N: int, L: int) -> List[List[int]]:
        self.answer = []
        self.N = N
        cur = []
        for i in range(1, N - L + 2):
            cur.append(i)
            self.traverse(i, L - 1, cur)
            cur.pop()
        return self.answer
