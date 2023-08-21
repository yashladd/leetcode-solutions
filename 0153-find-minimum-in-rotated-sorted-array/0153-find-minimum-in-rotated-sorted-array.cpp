class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size() ;
        int l = 0, h = n - 1;
        int mini = INT_MAX;
        while(l <= h){
            int m = (l + h) >> 1;
            // if arr already sorted ans will be arr[l]
            if(nums[l] <= nums[h]){
                mini = min( mini, nums[l]);
                break;
            }
            
            if(nums[l] <= nums[m]) {
                mini = min(mini, nums[l]);
                l = m + 1;
            } else {
                mini = min(mini, nums[m]);
                h = m - 1;
            }
        }
        return mini;
    }
};