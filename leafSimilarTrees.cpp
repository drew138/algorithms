// problem:
// https://leetcode.com/problems/leaf-similar-trees/submissions/856732619/
// Runtime
// 15 ms
// Beats
// 5.83%
// Memory
// 12.9 MB
// Beats
// 27.66%

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
  void dfs(TreeNode *root, vector<int> &seq) {
    if (!root)
      return;
    if (!(root->left) && !(root->right))
      seq.push_back(root->val);
    dfs(root->left, seq);
    dfs(root->right, seq);
  }

  bool leafSimilar(TreeNode *root1, TreeNode *root2) {
    vector<int> first, second;
    dfs(root1, first);
    dfs(root2, second);
    bool ans = true;
    if (first.size() != second.size())
      return false;
    for (int i = 0; i < first.size(); ++i)
      if (first[i] != second[i])
        ans = false;
    return ans;
  }
};
