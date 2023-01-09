// problem:
// https://leetcode.com/problems/binary-tree-preorder-traversal/description/
// Runtime
// 0 ms
// Beats
// 100%
// Memory
// 8.4 MB
// Beats
// 44.83%

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
  vector<int> ans;
  void dfs(TreeNode *root) {
    if (!root)
      return;
    ans.push_back(root->val);
    dfs(root->left);
    dfs(root->right);
  }
  vector<int> preorderTraversal(TreeNode *root) {

    dfs(root);
    return ans;
  }
};
