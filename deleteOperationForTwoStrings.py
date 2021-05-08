# problem: https://leetcode.com/problems/delete-operation-for-two-strings/
# Runtime: 292 ms, faster than 70.25% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 16.1 MB, less than 76.40% of Python3 online submissions for Delete Operation for Two Strings.

class Solution:
    def lcs(self, word1, word2):
        n, m = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        l = self.lcs(word1, word2)
        return len(word1) + len(word2) - 2 * l
