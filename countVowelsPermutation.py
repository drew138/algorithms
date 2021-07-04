# problem: https://leetcode.com/problems/count-vowels-permutation/
# Runtime: 108 ms, faster than 85.31% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 14.2 MB, less than 94.33% of Python3 online submissions for Count Vowels Permutation.


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        mod = 10 ** 9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (u + e + i) % mod, (a +
                                                i) % mod, (o + e) % mod, i % mod, (o + i) % mod
        return sum((a, e, i, o, u)) % mod
