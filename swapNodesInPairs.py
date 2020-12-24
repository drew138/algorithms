# problem: https: // leetcode.com/problems/swap-nodes-in-pairs/
# Runtime: 24 ms, faster than 94.63 % of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.3 MB, less than 10.51 % of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        cur = head.next
        temp = cur.next
        head.next = temp
        cur.next = head
        first = cur
        prev = head
        head = head.next
        while head:
            cur = head.next
            temp = cur.next if cur else None
            head.next = temp
            if cur:
                prev.next = cur
                cur.next = head
            prev = head
            head = head.next
        return first
