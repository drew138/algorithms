# problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# Runtime: 227 ms, faster than 31.55% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.1 MB, less than 96.32% of Python3 online submissions for First Unique Character in a String.


from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
