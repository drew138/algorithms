# problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Runtime: 57 ms, faster than 67.72% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.7 MB, less than 14.14% of Python3 online submissions for Reverse Words in a String III.


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda x: x[::-1], s.split())))
