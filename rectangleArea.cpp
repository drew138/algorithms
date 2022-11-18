// problem: https://leetcode.com/problems/rectangle-area/submissions/
// Runtime: 10 ms, faster than 78.64% of C++ online submissions for Rectangle
// Area. Memory Usage: 6 MB, less than 31.48% of C++ online submissions for
// Rectangle Area.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2,
                  int by2) {
    int bottom_y = max(ay1, by1);
    int bottom_x = max(ax1, bx1);
    int top_y = min(ay2, by2);
    int top_x = min(ax2, bx2);
    bool condition = top_x > bottom_x && top_y > bottom_y;
    int common = condition ? (top_x - bottom_x) * (top_y - bottom_y) : 0;
    int first = (ay2 - ay1) * (ax2 - ax1);
    int second = (by2 - by1) * (bx2 - bx1);
    return first + second - common;
  }
};
