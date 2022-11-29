# problem: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Runtime: 1248 ms, faster than 28.17% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 61.6 MB, less than 15.00% of Python3 online submissions for Insert Delete GetRandom O(1).

import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        n = len(self.nums)
        i = self.dict[val]
        self.nums[i], self.nums[n - 1] = self.nums[n - 1], self.nums[i]
        self.nums.pop()
        if i != n - 1:
            self.dict[self.nums[i]] = i
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
