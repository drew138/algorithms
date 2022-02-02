# problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Runtime: 200 ms, faster than 37.84% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.3 MB, less than 41.94% of Python3 online submissions for Find All Anagrams in a String.

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter, defaultdict
        counter = Counter(p)
        cur = defaultdict(int)
        n, m = len(s), len(p)
        tmp = m
        sol = []
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
                    sol.append(i)      
            else:
                cur = defaultdict(int)
                tmp = m
                j = i - 1
            i -= 1
        return sol