# problem: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# Runtime: 46 ms, faster than 70.17% of Python3 online submissions for Insert into a Sorted Circular Linked List.
# Memory Usage: 14.8 MB, less than 58.52% of Python3 online submissions for Insert into a Sorted Circular Linked List.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> 'Node':
        if not head:
            
            node = Node(insertVal)
            node.next = node
            return node
        
        cur = head
        while cur.next is not head:
            condition_one = cur.val <= cur.next.val and cur.val <= insertVal <= cur.next.val
            condition_two = cur.val > cur.next.val and cur.val <= insertVal
            condition_three = cur.val > cur.next.val and cur.val > insertVal < cur.next.val
            if condition_one or condition_two or condition_three:
                break
            cur = cur.next
        
        tmp = cur.next
        cur.next = Node(insertVal)
        cur.next.next = tmp
        
        return head
        
        