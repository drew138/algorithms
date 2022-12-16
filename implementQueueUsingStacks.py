# problem: https://leetcode.com/problems/implement-queue-using-stacks/description/
# Runtime
# 28 ms
# Beats
# 96.60%
# Memory
# 14 MB
# Beats
# 76.9%


class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        if self.second:
            return self.second.pop()

        self.first.reverse()
        self.second = self.first
        self.first = []
        return self.second.pop() if self.second else -1

    def peek(self) -> int:
        if self.second:
            return self.second[-1]

        self.first.reverse()
        self.second = self.first
        self.first = []
        return self.second[-1] if self.second else -1

    def empty(self) -> bool:
        return not self.first and not self.second


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
