class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size() ;
        vector<int> pref(n+1, 1);
        vector<int> suff(n+1, 1);
        int p=1, s = 1;
        for (int i = 0; i < n; i++){
            int k = nums[i];
            pref[i] = k * p;
            p = pref[i];
            suff[n-1-i] = s * nums[n-1-i];
            s = s * nums[n-1-i];
        }
        vector<int> ans(n);
        for (int i = 0; i < n; i++){
            if (i == 0){
                ans[i] = 1 * suff[1];
            }else {
                ans[i] = pref[i-1] * suff[i+1];
            }
        }
        return ans;
        
    }
};