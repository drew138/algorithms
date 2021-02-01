// problem: https://leetcode.com/problems/number-of-1-bits/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of 1 Bits.
// Memory Usage: 5.9 MB, less than 80.64% of C++ online submissions for Number of 1 Bits.

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        int answer = 0;
        int iterations = 32;
        while (iterations)
        {
            answer += n & 1;
            n >>= 1;
            iterations--;
        }
        return answer;
    }
};