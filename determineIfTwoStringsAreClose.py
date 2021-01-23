# problem: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Runtime: 436 ms, faster than 8.82% of Python3 online submissions for Determine if Two Strings Are Close.
# Memory Usage: 15.5 MB, less than 27.95% of Python3 online submissions for Determine if Two Strings Are Close.


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        from collections import defaultdict
        c1 = [0] * 26
        c2 = [0] * 26
        for s1, s2 in zip(word1, word2):
            c1[ord(s1) - 97] += 1
            c2[ord(s2) - 97] += 1
        for i in range(26):
            if c1[i] and not c2[i] or c2[i] and not c1[i]:
                return False
        m = defaultdict(int)
        c1.sort()
        c2.sort()
        return c1 == c2
