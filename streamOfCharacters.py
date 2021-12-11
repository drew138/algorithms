# problem: https://leetcode.com/problems/stream-of-characters/
# Runtime: 576 ms, faster than 83.23% of Python3 online submissions for Stream of Characters.
# Memory Usage: 40.2 MB, less than 39.97% of Python3 online submissions for Stream of Characters.


from collections import deque
from typing import List

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            self.add_word(word[::-1])
        self.characters = deque()

    def add_word(self, word):
        cur = self.trie
        for character in word:
            if character not in cur:
                cur[character] = {}
            cur = cur[character]
        cur["."] = None
        
    def check_word(self, word):
        cur = self.trie
        for character in word:
            if not cur:
                return False
            if "." in cur:
                return True
            if character in cur:
                cur = cur[character]
            else:
                return False
            
        return "." in cur
        

    def query(self, letter: str) -> bool:
        self.characters.appendleft(letter)
        return self.check_word(self.characters)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)