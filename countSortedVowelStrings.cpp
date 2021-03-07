// problem: https://leetcode.com/problems/count-sorted-vowel-strings/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Count Sorted Vowel Strings.
// Memory Usage: 5.8 MB, less than 96.91% of C++ online submissions for Count Sorted Vowel Strings.

typedef unsigned long long ll;

class Solution
{
public:
    int combination(ll n, ll r)
    {
        ll divisor = 1, dividend = 1;
        for (ll i = n - r + 1; i <= n; ++i)
        {
            dividend *= i;
        }
        for (ll i = 1; i <= r; ++i)
        {
            divisor *= i;
        }
        return (int)(dividend / divisor);
    }

    int countVowelStrings(int n)
    {
        return combination((ll)(n + 4), (ll)(4));
    }
};