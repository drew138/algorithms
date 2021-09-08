# problem: https://leetcode.com/problems/shifting-letters/
# Runtime: 832 ms, faster than 51.06% of Python3 online submissions for Shifting Letters.
# Memory Usage: 27.7 MB, less than 30.71% of Python3 online submissions for Shifting Letters.


import itertools
from typing import List


class Solution:
    def shiftCharacter(self, character, shift):
        shift = shift % 26
        character = (shift + ord(character) - 97) % 26
        character += 97
        return chr(character)

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        shifts = list(itertools.accumulate(shifts))
        shifts.reverse()
        l = list(s)
        for i in range(len(shifts)):
            l[i] = self.shiftCharacter(l[i], shifts[i])

        return "".join(l)
