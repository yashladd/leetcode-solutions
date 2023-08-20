class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int  n = nums.size();
        int l = 0, h = n-1;
        vector<int> ans (2, -1);
        while(l <= h){
            int m = (l + h) >> 1;
            if(nums[m] == target){
                int lft = m, rgt = m;
                while(lft-1 >= 0 && nums[lft-1] == target) {
                    lft--;
                }
                while(rgt+1 < n && nums[rgt+1] == target) {
                    rgt++;
                };
                for (int j = 0; j < ans.size(); j++){
                    if(j==0){
                        ans[j] = lft;
                    }else ans[j] = rgt;
                }
                return ans;
            } else if(nums[m] < target){
                l = m + 1;
            } else {
                h = m-1;
            }
        }
        return ans;
    }
};