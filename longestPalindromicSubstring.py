# problem: https://leetcode.com/problems/longest-palindromic-substring/submissions/
# Runtime: 2232 ms, faster than 34.97% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.5 MB, less than 24.33% of Python3 online submissions for Longest Palindromic Substring.


class Solution:

    def _valid(self, x, y):
        return x >= 0 and y < self.lenStr

    def _equalChar(self, x, y):
        return self.word[x] == self.word[y]

    def spreadBounds(self, index):
        a, b = index, index
        while self._valid(a, b) and self._equalChar(a, b):
            a -= 1
            b += 1
        a += 1
        b -= 1

        if self._valid(index, index + 1) and self._equalChar(index, index + 1):
            c, d = index, index + 1
            while self._valid(c - 1, d + 1) and self._equalChar(c - 1, d + 1):
                c -= 1
                d += 1
        else:
            c, d = index, index

        if b - a > d - c:
            return a, b
        else:
            return c, d

    def longestPalindrome(self, s: str) -> str:
        self.word = s
        self.lenStr = len(s)
        a, b = 0, 0
        for i in range(len(s)):
            x, y = self.spreadBounds(i)
            if y - x > b - a:
                a = x
                b = y
        return s[a:b+1]
