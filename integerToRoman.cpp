// problem: https://leetcode.com/problems/integer-to-roman/
// Runtime: 47 ms, faster than 8.46% of C++ online submissions for Integer to
// Roman. Memory Usage: 10.7 MB, less than 15.44% of C++ online submissions for
// Integer to Roman.

using namespace std;

#include <bits/stdc++.h>

class Solution {
public:
  string intToRoman(int num) {
    unordered_map<int, string> m = {
        {1, "I"},   {4, "IV"},   {5, "V"},    {9, "IX"},  {10, "X"},
        {40, "XL"}, {50, "L"},   {90, "XC"},  {100, "C"}, {400, "CD"},
        {500, "D"}, {900, "CM"}, {1000, "M"},
    };
    string ans = "";
    while (num) {
      int key;
      if (num >= 1000) {
        key = 1000;
      } else if (num >= 900) {
        key = 900;
      } else if (num >= 500) {
        key = 500;
      } else if (num >= 400) {
        key = 400;
      } else if (num >= 100) {
        key = 100;
      } else if (num >= 90) {
        key = 90;
      } else if (num >= 50) {
        key = 50;
      } else if (num >= 40) {
        key = 40;
      } else if (num >= 10) {
        key = 10;
      } else if (num >= 9) {
        key = 9;
      } else if (num >= 5) {
        key = 5;
      } else if (num >= 4) {
        key = 4;
      } else if (num >= 1) {
        key = 1;
      }
      num -= key;
      ans += m[key];
    }
    return ans;
  }
};
