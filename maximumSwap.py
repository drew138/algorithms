# problem: https://leetcode.com/problems/maximum-swap/
# Runtime: 32 ms, faster than 85.69% of Python3 online submissions for Maximum Swap.
# Memory Usage: 13.8 MB, less than 76.81% of Python3 online submissions for Maximum Swap.

class Solution:
    def get_max(self, digits, i, j, num):
        return num + ((digits[j] - digits[i]) * 10 ** i) + ((digits[i] - digits[j]) * 10 ** j)
        
    def maximumSwap(self, num: int) -> int:
        digits = []
        answer = num
        k = num
        while k:
            digit = k % 10
            k //= 10
            digits.append(digit) 
        cur_max = 0
        n = len(digits)
        for i in range(1, n):
            answer = max(answer, self.get_max(digits, i, cur_max, num))
            if digits[i] > digits[cur_max]:
                cur_max = i
        return answer