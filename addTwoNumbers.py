
# problem: https://leetcode.com/problems/add-two-numbers-ii/submissions/
# Runtime: 68 ms, faster than 88.41% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumOne = 0
        sumTwo = 0
        while (l1 or l2):
            if l1:
                sumOne = (sumOne * 10) + l1.val
                l1 = l1.next
            if l2:
                sumTwo = (sumTwo * 10) + l2.val
                l2 = l2.next
        total = sumOne + sumTwo
        cur = None
        if total == 0:
            head = ListNode()
        while total:
            digit = total % 10
            total //= 10
            head = ListNode(digit, cur)
            cur = head
        return head
