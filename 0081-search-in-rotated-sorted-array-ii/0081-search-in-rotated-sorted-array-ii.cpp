class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, h = nums.size() - 1;
        while (l <= h) {
            int m = (l + h) >> 1;
            if (nums[m] == target) return true;
            if(nums[l] == nums[m] && nums[m] == nums[h]){
                l++, h--;
            } else if(nums[l] <= nums[m]) {
                if (nums[l] <= target && nums[m] >= target){
                    h = m -1;
                } else {
                    l = m + 1;
                }
            } else {
                if (nums[m] <= target && nums[h] >= target) {
                    l = m + 1;
                } else {
                    h = m - 1;
                }
            }
        }
        return false;
    }
};