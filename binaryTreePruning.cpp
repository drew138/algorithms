// problem: https://leetcode.com/problems/binary-tree-pruning/
// Runtime: 2 ms, faster than 73.40% of C++ online submissions for Binary Tree
// Pruning. Memory Usage: 8.9 MB, less than 21.01% of C++ online submissions for
// Binary Tree Pruning.

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
  bool traverse(TreeNode *node) {
    if (!node)
      return false;
    bool left = traverse(node->left);
    if (!left)
      node->left = nullptr;
    bool right = traverse(node->right);
    if (!right)
      node->right = nullptr;
    return left | right | node->val == 1;
  }

  TreeNode *pruneTree(TreeNode *root) {
    bool tmp = traverse(root);
    if (!tmp)
      return nullptr;
    return root;
  }
};
