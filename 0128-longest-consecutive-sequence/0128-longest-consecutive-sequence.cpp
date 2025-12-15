class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        unordered_set<int> s;
        for (auto n: nums){
            s.insert(n);
        }
        int maxi = 1;
        for (auto n: nums) {
            if (s.find(n-1) == s.end()){
                int cnt = 1;
                int g = n+1;
                while (s.find(g) != s.end()) g++, cnt++;
                maxi = max(maxi, cnt);
            }
        }
        return maxi;
    }
};