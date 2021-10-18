# problem: https://leetcode.com/problems/cousins-in-binary-tree/
# Runtime: 32 ms, faster than 77.85% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 14.3 MB, less than 41.10% of Python3 online submissions for Cousins in Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node, parent, depth=0):
        if not node:
            return

        if node.val == self.x:
            self.xd = depth
            self.xp = parent
        elif node.val == self.y:
            self.yd = depth
            self.yp = parent

        self.traverse(node.right, node.val, depth + 1)
        self.traverse(node.left, node.val, depth + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x, self.y = x, y
        self.xd, self.yd = None, None
        self.xp, self.yp = None, None
        self.traverse(root, None)
        print(self.xd, self.yd, self.xp, self.yp)
        return self.xd == self.yd and self.xp != self.yp
