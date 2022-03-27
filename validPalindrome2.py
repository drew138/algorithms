# problem: https://leetcode.com/problems/valid-palindrome-ii/
# Runtime: 184 ms, faster than 51.59% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.5 MB, less than 52.96% of Python3 online submissions for Valid Palindrome II.


class Solution:
    def is_palindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.is_palindrome(l + 1, r, s) or self.is_palindrome(l, r - 1, s)
            r -= 1
            l += 1
        return True