# problem: https://leetcode.com/problems/linked-list-cycle/submissions/
# Runtime: 40 ms, faster than 96.50% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.2 MB, less than 13.00% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        turt = head
        rabbit = head
        while turt and rabbit:
            turt = turt.next
            rabbit = rabbit.next
            if not rabbit:
                break
            rabbit = rabbit.next
            if turt is rabbit:
                return True

        return False
