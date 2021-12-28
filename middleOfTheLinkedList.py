# problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Runtime: 32 ms, faster than 60.47% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 14.1 MB, less than 75.12% of Python3 online submissions for Middle of the Linked List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next
            if runner:
                runner = runner.next
        return walker