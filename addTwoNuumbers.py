# problem: https://leetcode.com/problems/add-two-numbers/
# Runtime: 64 ms, faster than 89.50% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 66.48% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        stack1.reverse()
        stack2.reverse()
        carry = 0
        head = None
        while stack1 or stack2:
            digitOne = stack1.pop() if stack1 else 0
            digitTwo = stack2.pop() if stack2 else 0
            num = digitOne + digitTwo + carry
            digit = num % 10
            carry = num // 10
            tmp = ListNode(val=digit, next=head)
            head = tmp
        if carry:
            head = ListNode(val=carry, next=head)
        prev = None
        while head:
            tmp = head.next
            cur = head
            cur.next = prev
            prev = cur
            head = tmp
        return prev
