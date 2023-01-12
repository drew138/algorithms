// problem:
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/
// Runtime
// 593 ms
// Beats
// 83.57%
// Memory
// 216.6 MB
// Beats
// 61.43%
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string labels;
  vector<int> dfs(vector<vector<int>> &adj, int node, vector<int> &ans,
                  vector<bool> &visited) {
    visited[node] = true;
    vector<int> tmp(26, 0);
    for (int child : adj[node]) {
      if (!visited[child]) {
        vector<int> cur = dfs(adj, child, ans, visited);
        for (int i = 0; i < 26; ++i) {
          tmp[i] += cur[i];
        }
      }
    }
    ans[node] = ++tmp[labels[node] - 'a'];
    return tmp;
  }

  vector<int> countSubTrees(int n, vector<vector<int>> &edges, string labels) {
    vector<vector<int>> adj(n, vector<int>());
    for (const auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }
    vector<bool> visited(n, false);
    vector<int> ans(n, 0);
    this->labels = labels;

    dfs(adj, 0, ans, visited);
    return ans;
  }
};
