# problem: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Runtime: 324 ms, faster than 75.11% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Memory Usage: 27.5 MB, less than 19.83% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num = 2 ** k
        combs = set()
        for i in range(len(s) - k+1):
            combs.add(s[i:i+k])
        return len(combs) == num
