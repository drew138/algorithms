// problem: https://leetcode.com/problems/network-delay-time/
// Runtime: 129 ms, faster than 81.59% of C++ online submissions for Network Delay Time.
// Memory Usage: 39.9 MB, less than 82.91% of C++ online submissions for Network Delay Time.
#include <bits/stdc++.h>
using namespace std;

class Compare {
    public:
    bool operator() (pair<int, int> &a, pair<int, int> &b)
    {
        return a.second < b.second;
    }
};

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        
        for (vector<int> &arr: times) {
            int from = arr[0] - 1, to = arr[1] - 1, w = arr[2];
            adj[from].push_back({to , w});
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
        pq.push({k - 1, 0});
        vector<int> answer(n, INT_MAX);
        answer[k -1] = 0;
        while (!pq.empty()) {
            pair<int, int> tmp = pq.top();
            int node = tmp.first, distance = tmp.second;
            pq.pop();
            for (auto &connection: adj[node]) {
                int new_distance = connection.second + distance;
                if (answer[connection.first] > new_distance) {
                    cout << new_distance << endl;
                    answer[connection.first] = new_distance;
                    pq.push({connection.first, new_distance});
                }
            }
        }
        int max_val = INT_MIN;
        for (int &val: answer) {
            cout << val << endl;
            max_val = max(max_val, val);
        }
        if (max_val == INT_MAX) return -1;
        return max_val;
    }
};
