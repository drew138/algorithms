# problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Runtime: 164 ms, faster than 61.44% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.5 MB, less than 34.55% of Python3 online submissions for Intersection of Two Linked Lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def traverse(self, node, dif):
        while dif:
            node = node.next
            dif -= 1
        return node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        pathA, pathB = headA, headB
        while pathA != None:
            pathA = pathA.next
            lenA += 1
        while pathB != None:
            pathB = pathB.next
            lenB += 1
        dif = abs(lenA - lenB)
        if lenA > lenB:
            headA = self.traverse(headA, dif)
        else:
            headB = self.traverse(headB, dif)
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
