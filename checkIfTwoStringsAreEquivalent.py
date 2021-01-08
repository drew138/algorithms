# problem: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Runtime: 32 ms, faster than 68.09% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 14.2 MB, less than 86.98% of Python3 online submissions for Check If Two String Arrays are Equivalent.

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
