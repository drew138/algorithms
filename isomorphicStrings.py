# problem: https: // leetcode.com/problems/isomorphic-strings/
# Runtime: 36 ms, faster than 83.54 % of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.4 MB, less than 65.53 % of Python3 online submissions for Isomorphic Strings.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_chars = {}
        seen = set()
        for index, character in enumerate(s):
            if character in map_chars:
                prev = map_chars[character]
                map_chars[character] = t[index]
                if prev != map_chars[character]:
                    return False
            else:
                if t[index] in seen:
                    return False
                seen.add(t[index])
                map_chars[character] = t[index]

        return True
