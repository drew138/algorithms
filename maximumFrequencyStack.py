# problem: https://leetcode.com/problems/maximum-frequency-stack/
# Runtime: 332 ms, faster than 41.69% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.2 MB, less than 91.24% of Python3 online submissions for Maximum Frequency Stack.
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.stack = []
        self.map = defaultdict(int)
        self.max = 0

    def push(self, x: int) -> None:
        self.map[x] += 1
        self.max = max(self.max, self.map[x])
        if self.map[x] > len(self.stack):
            self.stack.append([])
        self.stack[self.map[x]-1].append(x)

    def pop(self) -> int:
        i = len(self.stack) - 1
        while self.stack[i] == []:
            self.stack.pop()
            i -= 1
        self.max = i + 1
        n = self.stack[i].pop()
        self.map[n] -= 1
        return n


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
