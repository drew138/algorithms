# problem: https://leetcode.com/problems/binary-trees-with-factors/
# Runtime: 787 ms, faster than 37.37% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 14.1 MB, less than 57.07% of Python3 online submissions for Binary Trees With Factors.


from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        dp = { k : 1 for k in arr }
        mod = 10 ** 9 + 7
        arr.sort()
        for i in range(n):
            for j in range(i):
                if (arr[i] / arr[j]) in dp:
                    dp[arr[i]] += (dp[arr[j]] * (dp[int(arr[i] / arr[j])])) % mod
                    dp[arr[i]] %= mod
        return sum(dp.values()) % mod
