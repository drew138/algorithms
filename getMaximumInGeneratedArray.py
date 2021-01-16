# problem: https://leetcode.com/problems/get-maximum-in-generated-array/
# Runtime: 32 ms, faster than 61.15% of Python3 online submissions for Get Maximum in Generated Array.
# Memory Usage: 14.1 MB, less than 69.67% of Python3 online submissions for Get Maximum in Generated Array.


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        arr = [0, 1]
        for i in range(2, n + 1):
            if i % 2:
                arr.append(arr[(i-1)//2] + arr[((i-1)//2) + 1])
            else:
                arr.append(arr[i // 2])
        return max(arr)
