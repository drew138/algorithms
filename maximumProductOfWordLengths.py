# problem: https://leetcode.com/problems/maximum-product-of-word-lengths/
# Runtime: 4552 ms, faster than 11.50% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.5 MB, less than 96.88% of Python3 online submissions for Maximum Product of Word Lengths.

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                cond = False
                for character in words[i]:
                    if character in words[j]:
                        cond = True
                if not cond:
                    answer = max(answer, len(words[i]) * len(words[j]))
        return answer
