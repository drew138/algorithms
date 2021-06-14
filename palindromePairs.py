# problem: https://leetcode.com/problems/palindrome-pairs/
# Runtime: 504 ms, faster than 84.40% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 19.6 MB, less than 28.65% of Python3 online submissions for Palindrome Pairs.


from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        from collections import defaultdict
        m = defaultdict(list)
        answer = set()
        for i, word in enumerate(words):
            m[word].append([0, i])
            for j in range(1, len(word)+1):
                suffix, prefix = word[:j], word[j:]
                if suffix == suffix[::-1]:
                    m[prefix].append([-(prefix != ""), i])
                if prefix == prefix[::-1]:
                    m[suffix].append([+(suffix != ""), i])

        for i, word in enumerate(words):
            for first, second in m[word[::-1]]:
                if i != second and first <= 0:
                    answer.add((i, second))
                if i != second and first >= 0:
                    answer.add((second, i))
        return answer
