// problem: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
// Runtime: 250 ms, faster than 71.37% of C++ online submissions for Nearest
// Exit from Entrance in Maze. Memory Usage: 48.5 MB, less than 9.10% of C++
// online submissions for Nearest Exit from Entrance in Maze.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool is_answer(int x, int y, int n, int m) {
    return x == 0 || x == n || y == 0 || y == m;
  }

  int nearestExit(vector<vector<char>> &maze, vector<int> &entrance) {
    int dir_x[] = {-1, 1, 0, 0};
    int dir_y[] = {0, 0, 1, -1};

    queue<pair<int, int>> q;
    q.push({entrance[0], entrance[1]});
    int n = maze.size(), m = maze[0].size();
    maze[entrance[0]][entrance[1]] = '+';
    int depth = 0;
    while (q.size()) {
      queue<pair<int, int>> tmp;
      while (q.size()) {
        auto cur = q.front();
        q.pop();
        for (int i = 0; i < 4; ++i) {
          int x = cur.first + dir_x[i];
          int y = cur.second + dir_y[i];
          bool in_bounds = 0 <= x && x < n && 0 <= y && y < m;
          bool is_traversable = in_bounds && maze[x][y] == '.';

          if (is_traversable) {
            maze[x][y] = '+';
            if (is_answer(x, y, n - 1, m - 1))
              return ++depth;
            tmp.push({x, y});
          }
        }
      }
      swap(q, tmp);
      depth++;
    }
    return -1;
  }
};
