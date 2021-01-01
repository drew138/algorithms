# problem: https://leetcode.com/problems/check-array-formation-through-concatenation/
# Runtime: 36 ms, faster than 91.45% of Python3 online submissions for Check Array Formation Through Concatenation.
# Memory Usage: 14.2 MB, less than 57.13% of Python3 online submissions for Check Array Formation Through Concatenation.

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i, j = 0, 1
        tups = set()
        for piece in pieces:
            tups.add(tuple(piece))
        while j <= len(arr):
            el = tuple(arr[i:j])
            if el in tups:
                tups.remove(el)
                i = j
            j += 1
        return not tups
