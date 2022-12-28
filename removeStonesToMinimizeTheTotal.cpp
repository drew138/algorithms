// problem:
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
// Runtime
// 741 ms
// Beats
// 71.38%
// Memory
// 105 MB
// Beats
// 28.79%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int minStoneSum(vector<int> &piles, int k) {
    priority_queue<int> pq;
    for (int i = 0; i < piles.size(); ++i)
      pq.push(piles[i]);
    while (pq.size() && k) {
      auto top = pq.top();
      pq.pop();
      top -= top / 2;
      k--;
      if (top)
        pq.push(top);
    }
    int total = 0;
    while (pq.size()) {
      total += pq.top();
      pq.pop();
    }
    return total;
  }
};
