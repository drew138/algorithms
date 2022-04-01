# problem: https://leetcode.com/problems/reverse-string/submissions/
# Runtime: 240 ms, faster than 63.66% of Python3 online submissions for Reverse String.
# Memory Usage: 18.5 MB, less than 21.46% of Python3 online submissions for Reverse String.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            