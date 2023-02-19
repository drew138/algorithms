// problem:
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
// Runtime
// 3 ms
// Beats
// 73.66%
// Memory
// 12 MB
// Beats
// 93.95%

#include <bits/stdc++.h>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
    vector<vector<int>> ans;
    queue<TreeNode *> q, other;
    bool flag = false;
    if (root)
      q.push(root);
    while (q.size()) {
      vector<int> tmp;
      while (q.size()) {
        auto node = q.front();
        q.pop();
        tmp.push_back(node->val);
        if (node->left)
          other.push(node->left);
        if (node->right)
          other.push(node->right);
      }
      if (flag)
        reverse(tmp.begin(), tmp.end());
      ans.push_back(tmp);
      flag = !flag;
      swap(q, other);
    }
    return ans;
  }
};
