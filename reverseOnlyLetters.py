# problem: https://leetcode.com/problems/reverse-only-letters/
# Runtime: 48 ms, faster than 9.00% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 14.4 MB, less than 16.97% of Python3 online submissions for Reverse Only Letters.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            a = s[i]
            b = s[j]
            if not ((97 <= ord(a) <= 122) or (65 <= ord(a) <= 90)):
                i += 1
                continue
            if not ((97 <= ord(b) <= 122) or (65 <= ord(b) <= 90)):
                j -= 1
                continue
            s[i], s[j] = b, a
            i += 1
            j -= 1
        return "".join(s)
