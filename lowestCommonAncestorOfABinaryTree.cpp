// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
// Runtime: 20 ms, faster than 73.61% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
// Memory Usage: 14.2 MB, less than 57.81% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.

#include <bits/stdc++>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return root;
        
        if (root == p || root == q) {
            return root;
        }
        TreeNode* left = lowestCommonAncestor(root -> left, p, q);
        TreeNode* right = lowestCommonAncestor(root -> right, p, q);
        if (left && right) return root;
        if (left) return left;
        if (right) return right;
        return nullptr;
    }
};
