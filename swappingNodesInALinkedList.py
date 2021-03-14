# problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Runtime: 1072 ms, faster than 75.37% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.8 MB, less than 86.55% of Python3 online submissions for Swapping Nodes in a Linked List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left = head
        right = head
        cur = head
        while k := k - 1:
            left = left.next
            cur = cur.next
        while cur.next:
            cur = cur.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head
