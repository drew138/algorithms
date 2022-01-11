# problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Runtime: 32 ms, faster than 92.41% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 14.6 MB, less than 39.83% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def sumRootToLeaf(self, root: Optional[TreeNode], p_val = 0) -> int:
        if not root:
            return 0
        v = (p_val << 1) + root.val
        if (not root.left) and (not root.right):
            return v
        l = self.sumRootToLeaf(root.left, v) if root.left else 0
        r = self.sumRootToLeaf(root.right, v) if root.right else 0
        return l + r
