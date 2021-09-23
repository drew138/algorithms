# problem: https://leetcode.com/problems/break-a-palindrome/
# Runtime: 28 ms, faster than 82.30% of Python3 online submissions for Break a Palindrome.
# Memory Usage: 14.2 MB, less than 75.76% of Python3 online submissions for Break a Palindrome.


class Solution:
    def canReplace(self, i, n, character):
        isOdd = n % 2 == 1
        condition = character != "a" or (i + 1) == n
        if isOdd:
            return i != n // 2 and condition
        else:
            return condition

    def getReplacement(self, i, n):
        return "a" if i != (n - 1) else "b"

    def breakPalindrome(self, palindrome: str) -> str:
        characters = list(palindrome)
        n = len(characters)
        for i, character in enumerate(characters):
            if self.canReplace(i, n, character):
                characters[i] = self.getReplacement(i, n)
                break
        answer = "".join(characters)
        return answer if answer != palindrome else ""
