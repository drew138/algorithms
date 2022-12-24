// problem: https://leetcode.com/problems/domino-and-tromino-tiling/description/
// Runtime
// 23 ms
// Beats
// 8.51%
// Memory
// 48.3 MB
// Beats
// 5.15%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int numTilings(int n) {
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    dp[n][n] = 1;
    int mod = 1e9 + 7;
    for (int i = n; i >= 0; --i) {
      for (int j = n; j >= 0; --j) {
        if (i == j) {
          if (i > 1) {
            dp[i - 2][j - 2] += dp[i][j];
            dp[i - 2][j - 2] %= mod;
            dp[i - 1][j - 2] += dp[i][j];
            dp[i - 1][j - 2] %= mod;
            dp[i - 2][j - 1] += dp[i][j];
            dp[i - 2][j - 1] %= mod;
          }
          if (i > 0) {
            dp[i - 1][j - 1] += dp[i][j];
            dp[i - 1][j - 1] %= mod;
          }
        } else if (i + 1 == j) {
          if (j > 1) {
            dp[i - 1][j - 2] += dp[i][j];
            dp[i - 1][j - 2] %= mod;
            dp[i][j - 2] += dp[i][j];
            dp[i][j - 2] %= mod;
          }

        } else if (j + 1 == i) {
          if (i > 1) {
            dp[i - 2][j - 1] += dp[i][j];
            dp[i - 2][j - 1] %= mod;

            dp[i - 2][j] += dp[i][j];
            dp[i - 2][j] %= mod;
          }
        }
      }
    }
    return dp[0][0];
  }
};
