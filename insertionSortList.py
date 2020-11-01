# problem: https://leetcode.com/problems/insertion-sort-list/submissions/
# Runtime: 1916 ms, faster than 17.70% of Python online submissions for Insertion Sort List.
# Memory Usage: 18.8 MB, less than 6.22% of Python online submissions for Insertion Sort List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        node = ListNode(head.val)
        head = head.next
        while head != None:
            if head.val <= node.val:
                temp = ListNode(head.val)
                temp.next = node
                node = temp
            else:
                cur = node
                while (cur.next != None) and (cur.next.val < head.val):
                    cur = cur.next

                temp = cur.next
                cur.next = ListNode(head.val, temp)
            head = head.next
        return node
