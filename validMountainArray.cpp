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

// problem: https://leetcode.com/problems/valid-mountain-array/submissions/
// Runtime: 56 ms, faster than 64.87% of C++ online submissions for Valid Mountain Array.
// Memory Usage: 22.8 MB, less than 75.85% of C++ online submissions for Valid Mountain Array.

class Solution
{
public:
    bool validMountainArray(vector<int> &A)
    {

        bool hasDecrease = false, hasIncrease = false, isEqual, isMountainRange;
        if (A.empty() || A.size() < 3 || A[0] > A[1])
            return false;
        int prevNum = A[0];
        for (int i = 0; i < A.size(); ++i)
        {
            isEqual = (i != 0) && A[i] == prevNum;
            isMountainRange = hasDecrease && A[i] >= prevNum;
            if (isEqual || isMountainRange)
                return false;
            if (prevNum > A[i] && i != 1)
                hasDecrease = true;
            if (prevNum < A[i])
                hasIncrease = true;
            prevNum = A[i];
        }
        return (hasDecrease && hasIncrease);
    }
};