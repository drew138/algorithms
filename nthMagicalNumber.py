# problem: https://leetcode.com/problems/nth-magical-number/
# Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Nth Magical Number.
# Memory Usage: 14.5 MB, less than 15.15% of Python3 online submissions for Nth Magical Number.

class Solution:
    
    def mcd(self, num1, num2):
        
        num1, num2 = max(num1, num2), min(num1, num2)
        mod = num1 % num2
        if mod == 0:
            return num2
        
        return self.mcd(num2, mod)
        
    
    def aux(self, a, b, lcm, mid):
        return mid // a + mid // b - mid // lcm
    
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        
        lcm = a * b / self.mcd(a, b)
        l, r = 0, n * min(a, b)


        while l < r:
            mid = (r - l) // 2 + l
            num = self.aux(a, b, lcm, mid)
            if num < n:
                mid += 1
                l = mid
            else:
                r = mid
        return mid % (10 ** 9 + 7)
