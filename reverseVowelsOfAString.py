# problem: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Runtime: 56 ms, faster than 54.80% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 15.4 MB, less than 33.36% of Python3 online submissions for Reverse Vowels of a String.


class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = {"a", "e", "i", "o", "u"}
        for c in s:
            if c.lower() in vowels:
                stack.append(c)
        li = list(s)
        for i, c in enumerate(li):
            if c.lower() in vowels:
                li[i] = stack.pop()
        return "".join(li)
