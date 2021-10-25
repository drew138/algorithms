# problem: https://leetcode.com/problems/min-stack/
# Runtime: 60 ms, faster than 82.80% of Python3 online submissions for Min Stack.
# Memory Usage: 18 MB, less than 80.67% of Python3 online submissions for Min Stack.


class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self) -> None:

        if self.stack[-1] == self.stack_min[-1]:
            self.stack_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
