# problem: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# Runtime: 70 ms, faster than 5.08% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
# Memory Usage: 14.4 MB, less than 15.40% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.

class Solution:

    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        stack = []
        for node in nodes:
            stack.append(node)
            while len(stack) >= 3 and stack[-3].isnumeric() and stack[-2] == "#" and stack[-1] == "#":
                stack.pop()
                stack.pop()
                stack[-1] = "#"
        if stack and stack[0] == "#":
            stack.pop()

        return not stack
