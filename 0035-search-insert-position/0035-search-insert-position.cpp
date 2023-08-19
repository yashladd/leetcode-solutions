class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size() - 1;
        int ans = INT_MAX;
        while(lo <= hi) {
            int mid = (lo + hi) >> 1;
            // if (nums[mid] == target){
            //     ans = mid;
                // hi = mid - 1;
            if(nums[mid] >= target) {
                ans = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        if (ans < nums.size()) return ans;
        return nums.size();
    }
};