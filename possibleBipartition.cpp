// problem: https://leetcode.com/problems/possible-bipartition/description/
// Runtime
// 425 ms
// Beats
// 58.65%
// Memory
// 65 MB
// Beats
// 64.27%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
    vector<int> colors(n, 0);
    vector<vector<int>> adj(n, vector<int>());
    for (auto const &p : dislikes) {
      adj[p[0] - 1].push_back(p[1] - 1);
      adj[p[1] - 1].push_back(p[0] - 1);
    }
    bool ans = true;
    for (int i = 0; i < n; ++i) {
      if (colors[i] == 0) {
        ans = ans && dfs(i, 1, adj, colors);
      }
    }
    return ans;
  }

  bool dfs(int node, int color, vector<vector<int>> &adj, vector<int> &colors) {
    colors[node] = color;
    bool ans = true;
    for (int child : adj[node]) {
      if (colors[child] != 0 && colors[child] != (-color))
        return false;
      else if (colors[child] == 0) {
        ans = ans && dfs(child, -color, adj, colors);
      }
    }
    return ans;
  }
};
