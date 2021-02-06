# problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Runtime: 32 ms, faster than 86.76% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 14.8 MB, less than 68.70% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def traverse(self, head):
        while head:
            if head.child and head.next:
                node = self.traverse(head.child)
                head.child.prev = head
                head.next.prev, head.next, node.next = node, head.child, head.next
                head.child = None
                head = node
            elif head.child:
                head.child.prev = head
                head.next = head.child
                head.child = None
            prev = head
            head = head.next
        return prev

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self.traverse(head)
        return head
