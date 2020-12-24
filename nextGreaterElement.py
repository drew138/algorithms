# problem: https://leetcode.com/problems/next-greater-element-iii/
# Runtime: 28 ms, faster than 74.38% of Python3 online submissions for Next Greater Element III.
# Memory Usage: 14.4 MB, less than 13.46% of Python3 online submissions for Next Greater Element III.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        from collections import deque
        stack = deque()
        num = str(n)
        digits = [char for char in num]
        stack.append(len(digits) - 1)
        swapped = False
        for i in range(len(digits) - 1, 0, -1):
            stack.append(i)
            if digits[i] > digits[i-1]:
                index = i
                while stack and int(digits[stack[0]]) <= int(digits[i-1]):
                    stack.popleft()
                j = stack.popleft()
                digits[j], digits[i-1] = digits[i-1], digits[j]
                swapped = True
                break
        if not swapped:
            return -1
        partition = digits[index:]
        partition.sort()
        num = int("".join(digits[:index] + partition))
        return num if num < 2147483647 else -1
