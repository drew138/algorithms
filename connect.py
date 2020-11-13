# problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/
# Runtime: 56 ms, faster than 91.76% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.6 MB, less than 50.20% of Python3 online submissions for Populating Next Right Pointers in Each Node.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = root
        while cur.left != None:
            temp = cur
            while cur != None:
                cur.left.next = cur.right
                cur.right.next = None if cur.next == None else cur.next.left
                cur = cur.next
            cur = temp.left

        return root
