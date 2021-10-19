# problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Runtime: 32 ms, faster than 71.02% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.3 MB, less than 13.33% of Python3 online submissions for Binary Tree Inorder Traversal.


from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            answer.append(node.val)
            traverse(node.right)
        traverse(root)
        return answer
