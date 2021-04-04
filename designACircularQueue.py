# problem: https://leetcode.com/problems/design-circular-queue/
# Runtime: 72 ms, faster than 43.71% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 14.8 MB, less than 68.17% of Python3 online submissions for Design Circular Queue.


class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self. bottom = 0
        self.queue = [None] * k
        self.numElements = 0

    def enQueue(self, value: int) -> bool:
        if self.numElements == len(self.queue):
            return False
        self.numElements += 1
        self.queue[self.bottom] = value
        self.bottom += 1
        if self.bottom == len(self.queue):
            self.bottom = 0
        return True

    def deQueue(self) -> bool:
        if not self.numElements:
            return False
        self.queue[self.front] = None
        self.front += 1
        self.numElements -= 1
        if self.front == len(self.queue):
            self.front = 0
        return True

    def Front(self) -> int:
        if self.numElements == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.numElements == 0:
            return -1
        index = self.bottom - 1 if self.bottom > 0 else len(self.queue) - 1
        return self.queue[index]

    def isEmpty(self) -> bool:
        return self.numElements == 0

    def isFull(self) -> bool:
        return self.numElements == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
