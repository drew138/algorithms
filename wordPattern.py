# problem: https://leetcode.com/problems/word-pattern/
# Runtime: 40 ms, faster than 31.07% of Python3 online submissions for Word Pattern.
# Memory Usage: 14.3 MB, less than 55.12% of Python3 online submissions for Word Pattern.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern): return False
        m_chars = {}
        m_words = {}
        for character, word in zip(pattern, words):
            if (character in m_chars and m_chars[character] != word) or (word in m_words and m_words[word] != character):
                return False
            else:
                m_words[word] = character
                m_chars[character] = word
        return True