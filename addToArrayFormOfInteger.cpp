// problem:
// https://leetcode.com/problems/add-to-array-form-of-integer/description/
// Runtime
// 23 ms
// Beats
// 94.54%
// Memory
// 27.3 MB
// Beats
// 66.17%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> addToArrayForm(vector<int> &num, int k) {
    int carry = 0;
    reverse(num.begin(), num.end());
    for (int i = 0; i < num.size(); ++i) {
      int tmp = carry + num[i] + (k % 10);
      num[i] = tmp % 10;
      carry = tmp / 10;
      k /= 10;
    }
    while (k != 0) {
      int tmp = carry + k % 10;
      carry = tmp / 10;
      num.push_back(tmp % 10);
      k /= 10;
    }
    if (carry != 0)
      num.push_back(carry);
    reverse(num.begin(), num.end());
    return num;
  }
};
