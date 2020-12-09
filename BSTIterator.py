# problems: https: // leetcode.com/problems/binary-search-tree-iterator/
# Runtime: 68 ms, faster than 91.66% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 20.7 MB, less than 67.90% of Python3 online submissions for Binary Search Tree Iterator.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        from collections import deque
        self.stack = deque()
        self.iterLeft(root)

    def next(self) -> int:

        node = self.stack.pop()
        if node.right:
            self.iterLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def iterLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
