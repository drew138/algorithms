# problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Runtime: 132 ms, faster than 86.66% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.8 MB, less than 26.17% of Python3 online submissions for Insert into a Binary Search Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        node = root
        while node.val != val:
            if node.val > val:
                node.left = node.left if node.left else TreeNode(val=val)
                node = node.left
            else:
                node.right = node.right if node.right else TreeNode(val=val)
                node = node.right
        return root