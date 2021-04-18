# problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Runtime: 28 ms, faster than 91.78% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.3 MB, less than 48.74% of Python3 online submissions for Remove Nth Node From End of List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        walker = head
        runner = head
        for _ in range(n):
            runner = runner.next
        prev = None
        while runner:
            prev = walker
            walker = walker.next
            runner = runner.next
        if prev:
            prev.next = walker.next
        elif walker == head:
            head = walker.next
        return head
