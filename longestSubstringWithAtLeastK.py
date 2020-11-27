# problem: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Runtime: 28 ms, faster than 94.41% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 14.4 MB, less than 17.04% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.k = k
        self.string = s
        return self.helper(0, len(s))

    def helper(self, i, j):
        if j - i < self.k:
            return 0
        counter = [0] * 26
        for x in range(i, j):
            counter[ord(self.string[x]) - 97] += 1
        for x in range(i, j):
            if counter[ord(self.string[x]) - 97] < self.k:
                a = x + 1
                while a < j and counter[ord(self.string[a]) - 97] < self.k:
                    a += 1
                return max(self.helper(i, x), self.helper(a, j))
        return j - i
