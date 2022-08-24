// problem: https://leetcode.com/problems/power-of-three/submissions/
// Runtime: 39 ms, faster than 38.01% of C++ online submissions for Power of
// Three. Memory Usage: 5.9 MB, less than 29.00% of C++ online submissions for
// Power of Three.
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool isPowerOfThree(int n) {
    if (n <= 0)
      return false;
    while (n % 3 == 0)
      n /= 3;
    return n == 1;
  }
};
