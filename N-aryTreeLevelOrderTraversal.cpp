// problem: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
// Runtime: 21 ms, faster than 95.32% of C++ online submissions for N-ary Tree
// Level Order Traversal. Memory Usage: 11.9 MB, less than 34.37% of C++ online
// submissions for N-ary Tree Level Order Traversal.

#include <bits/stdc++.h>

using namespace std;

// Definition for a Node.
class Node {
public:
  int val;
  vector<Node *> children;

  Node() {}

  Node(int _val) { val = _val; }

  Node(int _val, vector<Node *> _children) {
    val = _val;
    children = _children;
  }
};

class Solution {
public:
  vector<vector<int>> levelOrder(Node *root) {
    vector<vector<int>> ans;
    if (!root)
      return ans;
    queue<Node *> q, o;
    q.push(root);
    while (!q.empty()) {
      vector<int> tmp;
      while (!q.empty()) {

        Node *node = q.front();
        q.pop();
        tmp.push_back(node->val);
        for (auto const &child : node->children) {
          o.push(child);
        }
      }
      ans.push_back(tmp);
      swap(o, q);
    }
    return ans;
  }
};
