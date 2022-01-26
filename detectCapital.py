# problem: https://leetcode.com/problems/detect-capital/
# Runtime: 52 ms, faster than 19.70% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.2 MB, less than 75.02% of Python3 online submissions for Detect Capital.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].islower():
            return word[1:] == word[1:].lower()
        else:
            return word[1:] in [word[1:].lower(), word[1:].upper()]