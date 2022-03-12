# problem: https://leetcode.com/problems/is-subsequence/
# Runtime: 61 ms, faster than 21.96% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.8 MB, less than 92.79% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if not s: return True
        i = 0
        n = len(s)
        for character in t:
            if character == s[i]:
                i += 1
                if i == n: return True
            
            
            
        return False