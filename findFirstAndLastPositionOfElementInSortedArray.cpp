#include <bits/stdc++>

using namespace std;


class Solution {
public:
		int lower_bound(vector<int>& nums, int target) {
			int l = -1 , r = nums.size();
			while (l + 1 < r) {
				int mid = (r - l) / 2 + l;
				if (nums[mid] < target) {
					l = mid;	
				} else {
					r = mid;	
				}
			}
			return r;
		}

		int upper_bound(vector<int>& nums, int target) {
			int l = -1, r = nums.size();
			while (l + 1 < r) {
				int mid = (r - l) / 2 + l; 
				if (nums[mid] <= target) {
					l = mid;	
				} else {
					r = mid;	
				}
			}
			return l;
		}
    vector<int> searchRange(vector<int>& nums, int target) {
      if (!nums.size()) return vector<int> {-1, -1};
      int start, end;
      start = this -> lower_bound(nums, target);
      start = start >= 0 && start < nums.size() && nums[start] == target ? start : -1;
      end = this -> upper_bound(nums, target);
      end = end >= 0 && end < nums.size() && nums[end] == target ? end : -1;
      return vector<int> {start, end};
    }
};

