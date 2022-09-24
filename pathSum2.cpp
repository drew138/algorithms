// problem: https://leetcode.com/problems/path-sum-ii/
// Runtime: 15 ms, faster than 72.54% of C++ online submissions for Path Sum II.
// Memory Usage: 20.2 MB, less than 47.44% of C++ online submissions for Path
// Sum II.

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
  void dfs(TreeNode *root, vector<int> &stack, vector<vector<int>> &ans,
           int target) {
    if (!root)
      return;
    stack.push_back(root->val);
    if (!(root->left) && !(root->right) && target == root->val) {
      vector<int> tmp = stack;
      ans.push_back(tmp);
    }

    dfs(root->right, stack, ans, target - root->val);
    dfs(root->left, stack, ans, target - root->val);

    stack.pop_back();
  }

  vector<vector<int>> pathSum(TreeNode *root, int targetSum) {
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(root, stack, ans, targetSum);
    return ans;
  }
};
