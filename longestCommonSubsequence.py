# problem: https://leetcode.com/problems/longest-common-subsequence/
# Runtime: 676 ms, faster than 31.55% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 22.8 MB, less than 42.40% of Python3 online submissions for Longest Common Subsequence.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                hasPreviousRow = i - 1 >= 0
                hasPreviousColumn = j - 1 >= 0
                diagonal = dp[i-1][j -
                                   1] if hasPreviousRow and hasPreviousColumn else 0
                if text1[i] == text2[j]:
                    diagonal += 1
                up = dp[i-1][j] if hasPreviousRow else 0
                left = dp[i][j-1] if hasPreviousColumn else 0
                dp[i][j] = max(diagonal, up, left)
        return dp[-1][-1]
