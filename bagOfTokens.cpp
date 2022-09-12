// problem: https://leetcode.com/problems/bag-of-tokens/submissions/
// Runtime: 17 ms, faster than 15.74% of C++ online submissions for Bag of
// Tokens. Memory Usage: 10.6 MB, less than 27.64% of C++ online submissions for
// Bag of Tokens.

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int bagOfTokensScore(vector<int> &tokens, int power) {
    if (tokens.size() == 1)
      return power >= tokens[0];
    int cur = 0;
    int ans = 0;
    sort(tokens.begin(), tokens.end());
    int l = 0, r = tokens.size() - 1;
    while (l < r && (tokens[l] <= power || cur)) {
      while (tokens[l] <= power) {
        power -= tokens[l];
        cur++;
        l++;
      }
      ans = max(ans, cur);
      if (l < r && cur) {
        power += tokens[r];
        r--;
        cur--;
      }
    }
    return ans;
  }
};
