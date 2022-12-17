// problem:
// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
// Runtime
// 11 ms
// Beats
// 89.4%
// Memory
// 11.9 MB
// Beats
// 93.66%

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int evalRPN(vector<string> &tokens) {
    vector<long> nums;
    for (auto const &token : tokens) {
      if (token == "+") {
        long first = nums[nums.size() - 1];
        nums.pop_back();
        long second = nums[nums.size() - 1];
        nums.pop_back();
        nums.push_back(first + second);
      } else if (token == "-") {
        long first = nums[nums.size() - 1];
        nums.pop_back();
        long second = nums[nums.size() - 1];
        nums.pop_back();
        nums.push_back(second - first);
      } else if (token == "*") {
        long first = nums[nums.size() - 1];
        nums.pop_back();
        long second = nums[nums.size() - 1];
        nums.pop_back();
        nums.push_back(first * second);
      } else if (token == "/") {
        long first = nums[nums.size() - 1];
        nums.pop_back();
        long second = nums[nums.size() - 1];
        nums.pop_back();
        nums.push_back(second / first);
      } else {
        nums.push_back(stoi(token));
      }
    }
    return nums[0];
  }
};
