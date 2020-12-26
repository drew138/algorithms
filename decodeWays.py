# problem: https://leetcode.com/problems/decode-ways/
# Runtime: 24 ms, faster than 96.56% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.3 MB, less than 44.75% of Python3 online submissions for Decode Ways.

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            cur = s[i-1]
            prev = s[i-2:i]
            if int(cur) > 0:
                dp[i] += dp[i-1]
            if 10 <= int(prev) < 27:
                dp[i] += dp[i-2]
        return dp[-1]
