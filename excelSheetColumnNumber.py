# problem: https://leetcode.com/problems/excel-sheet-column-number/
# Runtime: 31 ms, faster than 90.50% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.9 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        sol = 0
        exp = 0
        for i in range(n - 1, -1, -1):
            sol += (ord(columnTitle[i]) - ord('A') + 1) * (26 ** exp)
            exp += 1
        return sol
