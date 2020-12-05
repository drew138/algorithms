# problem: https://leetcode.com/problems/valid-anagram/submissions/
# Runtime: 52 ms, faster than 39.04% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 42.98% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter
        char_map = Counter(s)

        for char in t:
            char_map[char] -= 1
        for val in char_map.values():
            if val != 0:
                return False
        return True
