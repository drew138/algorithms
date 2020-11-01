#include <bits/stdc++.h>

#define D(x) cout << #x << x << endl;
#define ios ios_base::sync_with_stdio(0), cin.tie(0);
#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define all(v) v.begin(), v.end()
#define allgreater(v) v.begin(), v.end(), greater<int>()
#define formap(map) for (const auto &[key, value] : map)
#define ms(ar, val) memset(ar, val, sizeof ar)
typedef long long ll;
typedef long double ld;

using namespace std;

// problem: https://leetcode.com/problems/reverse-integer/submissions/
// Runtime: 4 ms, faster than 49.50% of C++ online submissions for Reverse Integer.
// Memory Usage: 6.7 MB, less than 7.80% of C++ online submissions for Reverse Integer.

class Solution
{
public:
    int reverse(int x)
    {
        long answer = 0;
        long i = 10;
        bool isNeg = x < 0 ? true : false;
        long input = (long)x;
        if (isNeg)
            input = -input;
        while (i--)
        {
            if (pow(10, i) < input)
            {
                answer += (input % 10) * pow(10, i);
                input = input / 10;
            }
            if (answer > 2147483647)
                return 0;
        }
        answer += (input % 10);
        if (isNeg)
            answer = -answer;
        return answer;
    }
};