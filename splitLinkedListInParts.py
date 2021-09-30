# problem: https://leetcode.com/problems/split-linked-list-in-parts/
# Runtime: 40 ms, faster than 65.15% of Python3 online submissions for Split Linked List in Parts.
# Memory Usage: 14.8 MB, less than 43.43% of Python3 online submissions for Split Linked List in Parts.

from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        tmp = head
        count = 0
        answer = []
        while tmp:
            count += 1
            tmp = tmp.next
        size = count // k
        left_over = count % k if size else 0
        if not size:
            size = 1
        cur = head
        while k:
            additional_nodes = 1 if left_over else 0
            if left_over:
                left_over -= 1
            num_nodes = size + additional_nodes
            answer.append(cur)
            prev = cur
            while num_nodes:
                prev = cur
                if cur:
                    cur = cur.next
                num_nodes -= 1
            if prev:
                prev.next = None
            k -= 1
        return answer
