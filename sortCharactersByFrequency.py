# problem: https://leetcode.com/problems/sort-characters-by-frequency/
# Runtime: 59 ms, faster than 48.15% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 16.8 MB, less than 19.75% of Python3 online submissions for Sort Characters By Frequency.

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        pairs = list(counter.items())
        pairs.sort(key=lambda x: x[1], reverse=True)
        l = []
        for key, val in pairs:
            l += [key for _ in range(val)]
        return "".join(l)
