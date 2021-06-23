# problem: https://leetcode.com/problems/number-of-matching-subsequences/
# Runtime: 3688 ms, faster than 6.27% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.7 MB, less than 74.74% of Python3 online submissions for Number of Matching Subsequences.


from typing import List


class Solution:
    def isSubSequence(self, s, w):
        i, j = 0, 0
        while i < len(s) and j < len(w):
            if s[i] == w[j]:
                j += 1
            i += 1
        return j == len(w)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import Counter
        answer = 0
        counter = Counter(words)
        for w, q in counter.items():
            if self.isSubSequence(s, w):
                answer += q
        return answer
