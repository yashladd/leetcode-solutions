class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map <int, int> m;
        for (auto n: nums) m[n]++;
        vector<vector<int>> count(nums.size() + 1);
        for (auto it: m){
            count[it.second].push_back(it.first);
        }
        vector<int> ans;
        
        for (int i=count.size() -1; i >= 0; i--){
            if (ans.size() == k) break;
            for (auto n: count[i]){
                ans.push_back(n);
            }
        }
        
        return ans;
    }
};