# problem: https://leetcode.com/problems/basic-calculator-ii/submissions/
# Runtime: 160 ms, faster than 12.38% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 17.6 MB, less than 13.55% of Python3 online submissions for Basic Calculator II.


class Solution:
    def calculate(self, s: str) -> int:
        tmp = []
        i = 0
        while i < len(s):
            if s[i] == "/":
                prev = tmp.pop()
                j = i
                while not s[j].isnumeric():
                    j += 1
                i = j
                while j < len(s) and s[j].isnumeric():
                    j += 1
                tmp.append(int(prev) // int(s[i:j]))
                i = j
                continue
            elif s[i] == "*":
                prev = tmp.pop()
                j = i
                while not s[j].isnumeric():
                    j += 1
                i = j
                while j < len(s) and s[j].isnumeric():
                    j += 1
                tmp.append(int(prev) * int(s[i:j]))
                i = j
                continue
            elif s[i].isnumeric():
                j = i
                while j < len(s) and s[j].isnumeric():
                    j += 1
                tmp.append(int(s[i:j]))
                i = j - 1
            elif s[i] != " ":
                tmp.append(s[i])
            i += 1
        print(tmp)
        total = tmp[0]
        i = 1
        while i < len(tmp):
            if tmp[i] == "+":
                total += tmp[i+1]
                i += 2
                continue
            elif tmp[i] == "-":
                total -= tmp[i+1]
                i += 2
                continue
            i += 1
        return total
