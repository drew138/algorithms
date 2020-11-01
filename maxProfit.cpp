#include <bits/stdc++.h>

#define D(x) cout << #x << " = " << x << endl;
#define ios ios_base::sync_with_stdio(0), cin.tie(0);
#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define all(v) v.begin(), v.end()
#define allgreater(v) v.begin(), v.end(), greater<int>()
#define formap(map) for (const auto &[key, value] : map)
#define ms(ar, val) memset(ar, val, sizeof ar)
typedef long long ll;
typedef long double ld;

using namespace std;

// problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
// Runtime: 8 ms, faster than 95.77% of C++ online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 13.5 MB, less than 6.60% of C++ online submissions for Best Time to Buy and Sell Stock.

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.empty())
        {
            return 0;
        }

        int maxProfit = 0, currMin = prices[0], tempProfit;
        for (int i = 0; i < prices.size(); ++i)
        {
            currMin = min(currMin, prices[i]);
            tempProfit = prices[i] - currMin;
            maxProfit = max(maxProfit, tempProfit);
        }
        return maxProfit;
    }
};