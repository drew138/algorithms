# problem: https://leetcode.com/problems/unique-morse-code-words/submissions/
# Runtime: 32 ms, faster than 78.35% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 14 MB, less than 93.65% of Python3 online submissions for Unique Morse Code Words.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]
        combinations = set()
        for word in words:
            transformation = []
            for c in word:
                transformation.append(chars[ord(c) - 97])
            transformation = "".join(transformation)
            combinations.add(transformation)
        return len(combinations)
