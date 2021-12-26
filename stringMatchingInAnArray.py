# problem: https://leetcode.com/problems/string-matching-in-an-array/
# Runtime: 40 ms, faster than 65.06% of Python3 online submissions for String Matching in an Array.
# Memory Usage: 14.4 MB, less than 28.16% of Python3 online submissions for String Matching in an Array.

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for word_one in words:
            for word_two in words:
                if word_one != word_two and word_one in word_two:
                    ans.add(word_one)
        return list(ans)
