# problem: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Runtime: 432 ms, faster than 56.51% of Python3 online submissions for Longest Word in Dictionary through Deleting.
# Memory Usage: 16.5 MB, less than 95.78% of Python3 online submissions for Longest Word in Dictionary through Deleting.


from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s:
            return ""
        answers = []
        for word in d:
            if len(word) == 1 and not word in s:
                continue
            j = 0
            for i in range(len(s)):
                if j == len(word):
                    break
                if s[i] == word[j]:
                    j += 1
            j == len(word) and answers.append(word)
        answers.sort(key=lambda item: (-len(item), item))
        return answers[0] if answers else ""
