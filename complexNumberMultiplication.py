# problem: https://leetcode.com/problems/complex-number-multiplication/
# Runtime: 28 ms, faster than 78.54% of Python3 online submissions for Complex Number Multiplication.
# Memory Usage: 14.1 MB, less than 72.80% of Python3 online submissions for Complex Number Multiplication.

class Solution:

    def parseNumber(self, number):
        mid = number.index("+")
        print(mid)
        real = int(number[0:mid])
        imaginary = int(number[mid+1:(len(number)-1)])
        return real, imaginary

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = self.parseNumber(num1)
        r2, i2 = self.parseNumber(num2)
        return f'{r1*r2 + i1*i2 * -1}+{r1*i2 + i1*r2}i'
