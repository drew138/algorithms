# problem: https: // leetcode.com/problems/find-duplicate-file-in-system/
# Runtime: 88 ms, faster than 61.55% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 24.2 MB, less than 27.12% of Python3 online submissions for Find Duplicate File in System.

from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        answer = []
        for path in paths:
            directory = path.split()
            di, files = directory[0], directory[1:]
            for file in files:
                i = file.index("(")
                name = file[:i]
                content = file[i:len(file)-1]
                d[content].append(di + "/" + name)
        for val in d.values():
            if len(val) > 1:
                answer.append(val)
        return answer
