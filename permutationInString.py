# problem: https://leetcode.com/problems/permutation-in-string/
# Runtime: 141 ms, faster than 44.38% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.1 MB, less than 83.82% of Python3 online submissions for Permutation in String.


class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        from collections import Counter, defaultdict

        counter = Counter(p)
        cur = defaultdict(int)
        n, m = len(s), len(p)
        tmp = m
        i, j = n - 1, n - 1
        while i >= 0:
            character = s[i]
            if character in counter:
                cur[character] += 1
                tmp -= 1
                while j > i and cur[character] > counter[character]:
                    cur[s[j]] -= 1
                    tmp += 1
                    j -= 1

                if tmp == 0:
                    return True  
            else:
                cur = defaultdict(int)
                tmp = m
                j = i - 1
            i -= 1
        return False