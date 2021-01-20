# problem: https://leetcode.com/problems/flip-equivalent-binary-trees/
# Runtime: 32 ms, faster than 70.65% of Python3 online submissions for Flip Equivalent Binary Trees.
# Memory Usage: 14.2 MB, less than 87.69% of Python3 online submissions for Flip Equivalent Binary Trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, nodeTwo):
        if not node and not nodeTwo or not self.isInvertible:
            return
        nodeRight = node.right.val if node.right else None
        nodeLeft = node.left.val if node.left else None
        nodeTwoRight = nodeTwo.right.val if nodeTwo.right else None
        nodeTwoLeft = nodeTwo.left.val if nodeTwo.left else None
        if nodeRight == nodeTwoRight and nodeLeft == nodeTwoLeft:
            self.traverse(node.left, nodeTwo.left)
            self.traverse(node.right, nodeTwo.right)
        elif nodeRight == nodeTwoLeft and nodeLeft == nodeTwoRight:
            tmp = nodeTwo.left
            nodeTwo.left = nodeTwo.right
            nodeTwo.right = tmp
            self.traverse(node.left, nodeTwo.left)
            self.traverse(node.right, nodeTwo.right)
        else:
            self.isInvertible = False

    def flipEquiv(self, A: TreeNode, B: TreeNode) -> bool:
        self.isInvertible = True
        if (A and not B) or (B and not A):
            return False
        if not (A or B):
            return True
        if A.val != B.val:
            return False
        self.traverse(A, B)
        return self.isInvertible
