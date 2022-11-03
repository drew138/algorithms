# problem: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# Runtime: 2754 ms, faster than 61.72% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.
# Memory Usage: 38.4 MB, less than 25.84% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.

from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        base = 0
        best = 0
        total = 0
        for key, val in counter.items():
            other = key[1] + key[0]
            if key[0] == key[1]:
                if val % 2 == 1:
                    if val > base:
                        best += max(0, base - 1) * 2
                        base = val
                    else:
                        best += 2 * (val - 1)
                else:
                    best += 2 * val
            elif other in counter:
                other = counter[key[1] + key[0]]
                total += min(other, val) * 4
                counter[key[1] + key[0]] = 0
        return base * 2 + total + best
