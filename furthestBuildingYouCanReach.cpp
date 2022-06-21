// problem: https://leetcode.com/problems/furthest-building-you-can-reach/
// Runtime: 203 ms, faster than 20.42% of C++ online submissions for Furthest Building You Can Reach.
// Memory Usage: 53.7 MB, less than 77.22% of C++ online submissions for Furthest Building You Can Reach.
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < n - 1; ++i) {
            int diff = heights[i + 1] - heights[i]; 
            
            if (diff <= 0) {
                continue;
            }
            pq.push(diff);

            
            if (pq.size() > ladders) {
                int min = pq.top();
                pq.pop();
                bricks -= min;
            } 
            
            if (bricks < 0) {
                return i;
            }
            
        }
        return n - 1;
    }
};