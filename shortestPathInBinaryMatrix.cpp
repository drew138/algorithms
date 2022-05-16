// problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/
// Runtime: 194 ms, faster than 26.05% of C++ online submissions for Shortest Path in Binary Matrix.
// Memory Usage: 32.8 MB, less than 29.56% of C++ online submissions for Shortest Path in Binary Matrix.
#include <bits/stdc++.h>

using namespace std;

struct pair_hash
{
    std::size_t operator() (const std::pair<int, int> &pair) const
    {
        return pair.first ^ pair.second;
    }
};

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int dir_x[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dir_y[] = {-1, -0, 1, -1, 1, -1, 0, 1};
        unordered_map<pair<int,int>, int, pair_hash> m;
        queue<pair<int, int>> q;
        if (!grid[0][0]) q.push({0, 0});
        m[{0, 0}] = 1;
        while (!q.empty()) {
            auto position = q.front(); q.pop();
            int x = position.first, y = position.second;
            for (int i = 0; i < 8; ++i) {
                int a = dir_x[i], b = dir_y[i];
                if (0 <= x + a && x + a < n && 0 <= y + b && y + b < n && !grid[x + a][y + b]) {
                    grid[x + a][y + b] = 1;
                    q.push({x + a, y + b});
                    m[{x + a, y + b}] = m[{x, y}] + 1;
                }
            }
        }
        return m[{n - 1, n - 1}] ? m[{n - 1, n - 1}] : -1;
    }
};
