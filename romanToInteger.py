# problem: https://leetcode.com/problems/roman-to-integer/
# Runtime: 52 ms, faster than 46.95% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.3 MB, less than 29.55% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and m[s[i]] < m[s[i+1]]:
                answer += m[s[i+1]] - m[s[i]]
                i += 1
            else:
                answer += m[s[i]]
            i += 1
        return answer
