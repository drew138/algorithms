// problem:
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
// Runtime
// 0 ms
// Beats
// 100%
// Memory
// 7.1 MB
// Beats
// 53.11%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  double average(vector<int> &salary) {
    if (salary.size() < 3)
      return 0;
    long long total = 0;
    int min_num = INT_MAX, max_num = INT_MIN;
    for (auto const &num : salary) {
      total += num;
      min_num = min(min_num, num);
      max_num = max(max_num, num);
    }
    total -= min_num + max_num;
    return total / (double)(salary.size() - 2);
  }
};
