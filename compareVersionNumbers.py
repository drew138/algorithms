# problem: https://leetcode.com/problems/compare-version-numbers/
# Runtime: 49 ms, faster than 34.42% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
    
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        n, m = len(l1), len(l2)
        for n1, n2 in zip(l1, l2):
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        if len(l1) == len(l2): return 0
        elif len(l1) > len(l2):
            for i in range(min(n, m), max(n, m)):
                if l1[i] != 0:
                    return 1 
        else:
            for i in range(min(n, m), max(n, m)):
                if l2[i] != 0:
                    return -1
        return 0
