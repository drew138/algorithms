# problem: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Runtime: 140 ms, faster than 22.61% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 17.8 MB, less than 71.52% of Python3 online submissions for Convert Sorted List to Binary Search Tree.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMiddle(self, head):
        left = head
        walker = head
        runner = head
        prev = head
        while runner and runner.next:
            prev = walker
            walker = walker.next
            runner = runner.next
            if runner:
                runner = runner.next
        prev.next = None
        left = left if left != walker else None
        right = walker.next if walker else None
        return walker, left, right

    def traverse(self, node):
        if not node:
            return node
        mid, left, right = self.findMiddle(node)
        l = self.traverse(left)
        r = self.traverse(right)
        return TreeNode(val=mid.val, left=l, right=r)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        root = self.traverse(head)
        return root
