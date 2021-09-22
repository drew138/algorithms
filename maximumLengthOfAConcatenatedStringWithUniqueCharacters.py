# problem: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Runtime: 124 ms, faster than 51.15% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Memory Usage: 14.5 MB, less than 48.27% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.

from typing import List


class Solution:
    def dfs(self, words, index, word):
        self.answer = max(self.answer, len(word))
        if index == len(words):
            return
        chars_word = set(word)
        chars_cur = set(words[index])
        if not chars_word & chars_cur:
            self.dfs(words, index + 1, word + words[index])
        self.dfs(words, index + 1, word)

    def maxLength(self, arr: List[str]) -> int:
        words = []
        self.answer = 0
        for word in arr:
            seen = set()
            valid = True
            for character in word:
                if not character in seen:
                    seen.add(character)
                else:
                    valid = False
                    break
            if valid:
                words.append(word)
        self.dfs(words, 0, "")
        return self.answer
