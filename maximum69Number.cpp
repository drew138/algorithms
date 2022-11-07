// problem: https://leetcode.com/problems/maximum-69-number/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Maximum 69
// Number. Memory Usage: 6 MB, less than 45.85% of C++ online submissions for
// Maximum 69 Number.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int maximum69Number(int num) {
    string s = to_string(num);
    for (int i = 0; i < s.size(); ++i) {
      if (s[i] == '6') {
        s[i] = '9';
        break;
      }
    }
    return stoi(s);
  }
};
