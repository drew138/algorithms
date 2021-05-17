# problem: https://leetcode.com/problems/longest-string-chain/
# Runtime: 240 ms, faster than 28.37% of Python3 online submissions for Longest String Chain.
# Memory Usage: 16.1 MB, less than 14.83% of Python3 online submissions for Longest String Chain.

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        from collections import defaultdict
        words.sort(key=lambda x: len(x))
        m = defaultdict(int)
        answer = 0

        for w in words:
            m[w] = 1
            for i in range(len(w)):
                s = w[:i] + w[i+1:]
                m[w] = max(m[s] + 1, m[w])
                answer = max(m[w], answer)
        return answer
