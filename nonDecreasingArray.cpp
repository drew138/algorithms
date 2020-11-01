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
//question: https://leetcode.com/problems/non-decreasing-array/submissions/
// Runtime: 52 ms, faster than 74.80% of C++ online submissions for Non-decreasing Array.
// Memory Usage: 27.5 MB, less than 9.15% of C++ online submissions for Non-decreasing Array.
class Solution
{
public:
    bool checkPossibility(vector<int> &nums)
    {
        int numConversions = 0;
        for (int i = 0; i < nums.size() - 1; ++i)
        {
            if (numConversions > 1)
                return false;
            if (nums[i] > nums[i + 1])
            {

                if (i == 0)
                {
                    numConversions++;
                }
                else if (i == nums.size() - 2)
                {
                    numConversions++;
                }
                else
                {
                    if (nums[i + 1] >= nums[i - 1])
                    {
                        numConversions++;
                    }
                    else if (nums[i + 2] > nums[i])
                    {
                        numConversions++;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        return (numConversions == 0 || numConversions == 1);
    }
};