// problem: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
// Runtime: 598 ms, faster than 97.21% of C++ online submissions for Find
// Players With Zero or One Losses. Memory Usage: 197.6 MB, less than 16.88% of
// C++ online submissions for Find Players With Zero or One Losses.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<int>> findWinners(vector<vector<int>> &matches) {
    int n = 0;
    for (int i = 0; i < matches.size(); ++i) {
      n = max(n, matches[i][0]);
      n = max(n, matches[i][1]);
    }
    vector<int> counter(n + 1, -1);
    for (int i = 0; i < matches.size(); ++i) {
      auto tmp = matches[i];
      if (counter[tmp[0]] == -1)
        counter[tmp[0]] = 0;
      if (counter[tmp[1]] == -1)
        counter[tmp[1]] = 0;
      ++counter[tmp[1]];
    }
    vector<int> first, second;
    for (int i = 0; i < counter.size(); ++i) {
      if (counter[i] == 0) {
        first.push_back(i);
      } else if (counter[i] == 1) {
        second.push_back(i);
      }
    }
    return {first, second};
  }
};
