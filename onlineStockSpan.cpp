// problem: https://leetcode.com/problems/online-stock-span/
// Runtime: 545 ms, faster than 21.88% of C++ online submissions for Online
// Stock Span. Memory Usage: 84.1 MB, less than 90.79% of C++ online submissions
// for Online Stock Span.

#include <bits/stdc++.h>

using namespace std;

class StockSpanner {
public:
  vector<pair<int, int>> s;

  int next(int price) {
    int ans = 1;
    while (s.size() && s[s.size() - 1].first <= price) {
      pair<int, int> tmp = s[s.size() - 1];
      s.pop_back();
      ans += tmp.second;
    }
    s.push_back({price, ans});
    return ans;
  }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
