# problem: https://leetcode.com/problems/palindromic-substrings/
# Runtime: 184 ms, faster than 57.69% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 14.4 MB, less than 45.89% of Python3 online submissions for Palindromic Substrings.


class Solution:
    def getNumberOfPalindromes(self, i, j):
        while i >= 0 and j < len(self.s) and self.s[i] == self.s[j]:
            self.answer += 1
            i -= 1
            j += 1

    def countSubstrings(self, s: str) -> int:
        self.answer = 0
        self.s = s
        for i in range(len(s)):
            self.getNumberOfPalindromes(i, i)
            self.getNumberOfPalindromes(i, i + 1)

        return self.answer
