# problem: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
# Runtime: 432 ms, faster than 65.61% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 15.9 MB, less than 49.26% of Python3 online submissions for Smallest String With A Given Numeric Value.

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        word = ["a" for _ in range(n)]
        total = n
        i = n - 1
        while total < k:
            if k - total >= 25:
                total += 25
                word[i] = "z"
            else:
                word[i] = chr(97 + k - total)
                total = k
            i -= 1
        return "".join(word)
