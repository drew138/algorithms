// problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
// Runtime: 27 ms, faster than 44.26% of C++ online submissions for Delete Node
// in a Linked List. Memory Usage: 7.4 MB, less than 92.32% of C++ online
// submissions for Delete Node in a Linked List.

#include <bits/stdc++.h>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
  void deleteNode(ListNode *node) {
    ListNode *cur = node->next;
    ListNode *prev = node;
    while (cur) {
      prev->val = cur->val;
      if (!cur->next) {
        prev->next = nullptr;
        break;
      }
      ListNode *tmp = cur;
      cur = cur->next;
      prev = tmp;
    }
  }
};

// Alternate solution
// Runtime: 17 ms, faster than 75.69% of C++ online submissions for Delete Node
// in a Linked List. Memory Usage: 7.5 MB, less than 92.32% of C++ online
// submissions for Delete Node in a Linked List.
class Solution2 {
public:
  void deleteNode(ListNode *node) { swap(*node, *node->next); }
};
