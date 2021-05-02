# problem: https://leetcode.com/problems/prefix-and-suffix-search/
# Runtime: 752 ms, faster than 81.70% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 38.2 MB, less than 53.59% of Python3 online submissions for Prefix and Suffix Search.

from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.wordsIndex = {}
        for i in range(len(words)):
            w = words[i]
            n = len(w)
            for j in range(n, -1, -1):
                for k in range(n + 1):
                    self.wordsIndex[w[:j]+"#"+w[k:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        if prefix+"#"+suffix in self.wordsIndex:
            return self.wordsIndex[prefix+"#"+suffix]
        return -1
