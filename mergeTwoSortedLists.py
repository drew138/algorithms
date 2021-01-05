# problem: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Runtime: 40 ms, faster than 44.19% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.1 MB, less than 74.47% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            head = l1
            l1 = l1.next
        elif l2 and not l1:
            head = l2
            l2 = l2.next
        elif l1 and l2:
            if l1.val < l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
        else:
            head = None
        cur = head
        while l1 or l2:
            if l1 and not l2:
                cur.next = l1
                l1 = l1.next
            elif l2 and not l1:
                cur.next = l2
                l2 = l2.next
            elif l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            cur = cur.next
        return head
