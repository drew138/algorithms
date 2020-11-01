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

// problem: https://leetcode.com/problems/maximum-subarray/submissions/
// Runtime: 8 ms, faster than 97.02% of C++ online submissions for Maximum Subarray.
// Memory Usage: 13.5 MB, less than 19.67% of C++ online submissions for Maximum Subarray.

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        long maxSum = nums[0];
        long tempMax = maxSum;
        long temp, curr;
        for (int i = 0; i < nums.size(); ++i)
        {
            temp = tempMax + nums[i];
            curr = nums[i];
            if (i != 0)
                tempMax = max(curr, temp);
            maxSum = max(maxSum, tempMax);
        }
        return maxSum;
    }
};