# problem: https://leetcode.com/problems/string-to-integer-atoi/
# Runtime: 32 ms, faster than 86.89% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.2 MB, less than 81.96% of Python3 online submissions for String to Integer (atoi).

class Solution:
    
    def recognizeWhiteSpace(self, i, s):
        while i < len(s) and s[i] == ' ':
            i += 1
        return i
    
    def recognizeSign(self, i, s):
        if i < len(s) and s[i] == '-':
            return True, i + 1
        elif i < len(s) and s[i] == '+':
            i += 1
        return False, i
    
    def recognizeDigits(self, i, s, hasSign):
        cur = 0
        while i < len(s) and s[i].isnumeric():
            cur *= 10
            cur += int(s[i])
            i += 1
            if (not hasSign) and cur >= (2 ** 31 - 1):
                return 2 ** 31 - 1
            elif hasSign and  cur >= (2 ** 31):
                return 2 ** 31
        return cur
        
    def myAtoi(self, s: str) -> int:
        i = 0
        i = self.recognizeWhiteSpace(i, s)
        hasSign, i = self.recognizeSign(i, s)
        num = self.recognizeDigits(i, s, hasSign)
        if hasSign:
            num = - num
        return num