// problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
// Runtime: 3 ms, faster than 60.90% of C++ online submissions for Binary Tree
// Inorder Traversal. Memory Usage: 8.5 MB, less than 39.59% of C++ online
// submissions for Binary Tree Inorder Traversal.
// Definition for a binary tree node.

#include <bits/stdc++.h>

using namespace std;

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
  void dfs(TreeNode *node, vector<int> &ans) {
    if (!node)
      return;
    dfs(node->left, ans);
    ans.push_back(node->val);
    dfs(node->right, ans);
  }

  vector<int> inorderTraversal(TreeNode *root) {
    vector<int> ans;
    dfs(root, ans);
    return ans;
  }
};
