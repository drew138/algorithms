# problem: https: // leetcode.com/problems/word-ladder/
# Runtime: 656 ms, faster than 17.08 % of Python3 online submissions for Word Ladder.
# Memory Usage: 15.3 MB, less than 69.45 % of Python3 online submissions for Word Ladder.

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        wordSet = set(wordList)
        if not endWord in wordSet:
            return 0
        queue = deque()
        queue.append(beginWord)
        answer = 0
        level = 1
        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                chars = [c for c in word]
                for i in range(len(chars)):
                    cp = chars[i]
                    for j in range(26):
                        if cp == chr(97+j):
                            continue
                        chars[i] = chr(97+j)
                        string = "".join(chars)
                        if string == endWord:
                            return level
                        if string in wordSet:
                            queue.append(string)
                            wordSet.remove(string)
                    chars[i] = cp
        return 0
