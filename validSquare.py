# problem: https://leetcode.com/problems/valid-square/submissions/
# Runtime: 24 ms, faster than 98.00% of Python3 online submissions for Valid Square.
# Memory Usage: 14.1 MB, less than 99.78% of Python3 online submissions for Valid Square.

from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        from collections import defaultdict
        from math import sqrt

        numPerpendicular = 0
        distances = defaultdict(int)
        vectors = []
        coordinates = [p1, p2, p3, p4]
        hasFourEqual = False
        for i in range(4):
            for j in range(i + 1, 4):
                a, b = coordinates[i]
                c, d = coordinates[j]
                vectors.append([a - c, b - d])
        for vector in vectors:
            sizeVector = sqrt((vector[0]**2) + (vector[1]**2))
            distances[sizeVector] += 1
        for i in range(6):
            for j in range(i + 1, 6):
                a, b = vectors[i]
                c, d = vectors[j]
                if ((a * b) + (c * d)) == 0:
                    numPerpendicular += 1

        for values in distances.values():
            if values == 4:
                hasFourEqual = True
                break
        return ((numPerpendicular >= 4) and hasFourEqual)
