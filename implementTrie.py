# problem: https://leetcode.com/problems/implement-trie-prefix-tree/
# Runtime: 136 ms, faster than 88.22% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.9 MB, less than 85.31% of Python3 online submissions for Implement Trie (Prefix Tree).


from collections import defaultdict


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for character in word:
            if not character in cur:
                cur[character] = {}
            cur = cur[character]
        cur["."] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for character in word:
            if not character in cur:
                return False
            cur = cur[character]
        return "." in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for character in prefix:
            if not character in cur:
                return False
            cur = cur[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
