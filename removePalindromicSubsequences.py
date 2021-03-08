# problem: https://leetcode.com/problems/remove-palindromic-subsequences/
# Runtime: 32 ms, faster than 58.63% of Python3 online submissions for Remove Palindromic Subsequences.
# Memory Usage: 14.1 MB, less than 90.00% of Python3 online submissions for Remove Palindromic Subsequences.


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
