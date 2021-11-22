# problem: https://leetcode.com/problems/delete-node-in-a-bst/
# Runtime: 127 ms, faster than 7.27% of Python3 online submissions for Delete Node in a BST.
# Memory Usage: 18.5 MB, less than 22.29% of Python3 online submissions for Delete Node in a BST.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse_left(self, node):
        while node and node.left:
            node = node.left
        return node

    def modify(self, left, right):
        bottom_right = self.traverse_left(right)
        if bottom_right:
            bottom_right.left = left
        else:
            right = left
        return right

    def search(self, node, target):

        if not node:
            return None, False
        if node.val == target:

            return self.modify(node.left, node.right), True
        elif node.val > target:
            child, is_swap = self.search(node.left, target)
            if is_swap:
                node.left = child
        else:
            child, is_swap = self.search(node.right, target)
            if is_swap:
                node.right = child
        return None, False

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        ans, is_swap = self.search(root, key)
        return ans if is_swap else root
