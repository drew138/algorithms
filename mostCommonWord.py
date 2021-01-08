# problem: https: // leetcode.com/problems/most-common-word/
# Runtime: 52 ms, faster than 5.65 % of Python3 online submissions for Most Common Word.
# Memory Usage: 14.3 MB, less than 65.13 % of Python3 online submissions for Most Common Word.

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re
        banned = set(banned)
        words = [c.lower() for c in re.split(r"[!?',;. ]+", paragraph)
                 if not c.lower() in banned and c != ""]
        counter = Counter(words)
        answer = None
        maxNum = 0
        for key, val in counter.items():
            if val > maxNum:
                answer = key
                maxNum = val
        return answer
