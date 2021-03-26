# problem: https://leetcode.com/problems/word-subsets/
# Runtime: 1892 ms, faster than 5.03% of Python3 online submissions for Word Subsets.
# Memory Usage: 18 MB, less than 76.82% of Python3 online submissions for Word Subsets.

from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter

        answer = []
        counter = [0] * 26
        for w in B:
            c = Counter(w)
            for i in range(26):
                counter[i] = max(counter[i], c[chr(97+i)])
        for w in A:
            c = Counter(w)
            complies = True
            for i in range(26):
                if c[chr(97+i)] < counter[i]:
                    complies = False
                    break
            if complies:
                answer.append(w)
        return answer
