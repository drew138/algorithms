# problem: https://leetcode.com/problems/orderly-queue/
# Runtime: 32 ms, faster than 63.74% of Python3 online submissions for Orderly Queue.
# Memory Usage: 14.4 MB, less than 19.78% of Python3 online submissions for Orderly Queue.

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))
