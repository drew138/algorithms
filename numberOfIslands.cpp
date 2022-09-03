// problem: https://leetcode.com/problems/number-of-islands/
// Runtime: 66 ms, faster than 35.13% of C++ online submissions for Number of
// Islands. Memory Usage: 22.9 MB, less than 6.73% of C++ online submissions for
// Number of Islands.
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  void bfs(int x, int y, vector<vector<char>> &grid,
           vector<vector<bool>> &seen) {
    queue<pair<int, int>> q;
    q.push({x, y});
    seen[x][y] = true;
    while (!q.empty()) {
      pair<int, int> node = q.front();
      q.pop();
      vector<pair<int, int>> dirs = {{node.first + 1, node.second},
                                     {node.first, node.second + 1},
                                     {node.first - 1, node.second},
                                     {node.first, node.second - 1}};
      for (pair<int, int> p : dirs) {
        bool in_bounds = (0 <= p.first) && (p.first < grid.size()) &&
                         (0 <= p.second) && (p.second < grid[0].size());
        if (in_bounds && !seen[p.first][p.second] &&
            grid[p.first][p.second] == '1') {
          seen[p.first][p.second] = true;
          q.push(p);
        }
      }
    }
  }

  int numIslands(vector<vector<char>> &grid) {
    vector<vector<bool>> seen(grid.size(), vector<bool>(grid[0].size(), false));
    int ans = 0;
    for (int i = 0; i < grid.size(); ++i)
      for (int j = 0; j < grid[i].size(); ++j)
        if (!seen[i][j] && grid[i][j] == '1') {
          ++ans;
          bfs(i, j, grid, seen);
        }
    return ans;
  }
};
