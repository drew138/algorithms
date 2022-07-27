// problem:https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
// Runtime: 7 ms, faster than 81.17% of C++ online submissions for Flatten Binary Tree to Linked List.
// Memory Usage: 12.6 MB, less than 96.54% of C++ online submissions for Flatten Binary Tree to Linked List.

#include <bits/stdc++.h> 

using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* traverse(TreeNode* root) {
        if (!root) return root;
        
        TreeNode* cur = traverse(root -> left);
        TreeNode* tmp = root -> right;
        while (cur && cur -> right) cur = cur -> right;
        if (cur) {
            root -> right = root -> left;
            cur -> right = traverse(tmp);
        } else {
            root -> right = traverse(tmp);
        }
        root -> left = nullptr;
        return root;
    }
    
    void flatten(TreeNode* root) {
        traverse(root);
    }
};
