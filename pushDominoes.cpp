// https://leetcode.com/problems/push-dominoes/
// Runtime: 63 ms, faster than 61.01% of C++ online submissions for Push
// Dominoes. Memory Usage: 12.5 MB, less than 97.92% of C++ online submissions
// for Push Dominoes.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string pushDominoes(string dominoes) {
    int l = 0;
    for (int r = 0; r < dominoes.size(); ++r) {
      if (dominoes[r] == 'L' && (dominoes[l] == '.' || dominoes[l] == 'L')) {
        for (int i = l; i < r; ++i)
          dominoes[i] = 'L';
        l = r + 1;
      } else if (dominoes[r] == 'L' && dominoes[l] == 'R') {
        for (int i = l; i < r; ++i)
          dominoes[i] = i <= (r - l) / 2 + l ? 'R' : 'L';
        if ((r - l) % 2 == 0)
          dominoes[(r - l) / 2 + l] = '.';
        l = r + 1;
      } else if (dominoes[r] == 'R' && dominoes[l] == 'R') {
        for (int i = l; i < r; ++i)
          dominoes[i] = 'R';
        l = r;
      } else if (dominoes[r] == 'R') {
        l = r;
      }
    }
    if (l < dominoes.size() && dominoes[l] == 'R')
      for (int i = l; i < dominoes.size(); ++i)
        dominoes[i] = 'R';
    return dominoes;
  }
};
