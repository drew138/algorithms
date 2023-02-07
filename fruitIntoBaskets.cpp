// problem: https://leetcode.com/problems/fruit-into-baskets/description/
// Runtime
// 307 ms
// Beats
// 16.38%
// Memory
// 74 MB
// Beats
// 20.6%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int totalFruit(vector<int> &fruits) {
    int ans = 0;
    int i = 0, j = 0;
    int n = fruits.size();
    map<int, int> m;
    int total = 0;
    while (j < n) {
      int cur = fruits[j];
      if (total < 2 && m[cur] == 0) {
        total++;
        m[cur]++;
        j++;
      } else if (total <= 2 && m[cur] > 0) {
        m[cur]++;
        j++;
      } else {
        int tmp = fruits[i];
        m[tmp]--;
        if (m[tmp] == 0)
          total--;
        i++;
      }
      ans = max(j - i, ans);
    }
    return ans;
  }
};
