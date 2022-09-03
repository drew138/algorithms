// problem:
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/
//  Runtime: 0 ms, faster than 100.00% of C++ online submissions for Numbers
//  With Same Consecutive Differences. Memory Usage: 8.1 MB, less than 64.01% of
//  C++ online submissions for Numbers With Same Consecutive Differences.
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int generate_number(vector<int> &stack) {
    int cur = 0;
    for (int num : stack) {
      cur *= 10;
      cur += num;
    }
    return cur;
  }

  void traverse(vector<int> &ans, vector<int> &stack, int n, int k) {
    if (stack.size() == n) {
      int tmp = generate_number(stack);
      ans.push_back(tmp);
      return;
    }
    int last = stack[stack.size() - 1];
    if (last + k <= 9) {
      stack.push_back(last + k);
      traverse(ans, stack, n, k);
      stack.pop_back();
    }
    if (k == 0)
      return;
    if (last - k >= 0) {
      stack.push_back(last - k);
      traverse(ans, stack, n, k);
      stack.pop_back();
    }
  }

  vector<int> numsSameConsecDiff(int n, int k) {
    vector<int> ans, stack;

    for (int i = 1; i < 10; ++i) {
      stack.push_back(i);
      traverse(ans, stack, n, k);
      stack.pop_back();
    }
    return ans;
  }
};
