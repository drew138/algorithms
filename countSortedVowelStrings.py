# problem: https://leetcode.com/problems/count-sorted-vowel-strings/
# Runtime: 8268 ms, faster than 5.04% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.4 MB, less than 31.16% of Python3 online submissions for Count Sorted Vowel Strings.


class Solution:
    def traverse(self, vowel, level):
        level -= 1
        if not level:
            self.answer += 1
            return
        index = self.vowels.index(vowel)
        for i in range(index, 5):
            self.traverse(self.vowels[i], level)

    def countVowelStrings(self, n: int) -> int:
        self.answer = 0
        self.vowels = ["a", "e", "i", "o", "u"]
        for vowel in self.vowels:
            self.traverse(vowel, n)
        return self.answer
