# problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Runtime: 256 ms, faster than 52.99% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.4 MB, less than 62.91% of Python3 online submissions for Count Good Nodes in Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if not node:
                return 0
            total = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)
            right = dfs(node.right, max_value)
            left = dfs(node.left, max_value)
            return total + left + right
        return dfs(root, -float("inf"))
