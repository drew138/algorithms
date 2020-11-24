# problem: https://leetcode.com/problems/length-of-last-word/submissions/
# Runtime: 32 ms, faster than 36.23% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.2 MB, less than 72.50% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        numChars = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                numChars += 1
            elif numChars:
                break
        return numChars
