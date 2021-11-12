# problem: https://leetcode.com/problems/remove-linked-list-elements/
# Runtime: 68 ms, faster than 78.34% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.2 MB, less than 26.69% of Python3 online submissions for Remove Linked List Elements.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        walker = head
        new_list = ListNode()
        cur = new_list
        while walker:
            if walker.val != val:
                cur.next = walker
                cur = cur.next
            walker = walker.next
        if cur.next and cur.next.val == val:
            cur.next = None
        return new_list.next
