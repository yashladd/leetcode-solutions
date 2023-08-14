class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map <int, int> m;
        for (auto n: nums) m[n]++;
        priority_queue<pair<int,int>> pq;
        for (auto it: m){
            pq.push({it.second, -it.first});
        }
        vector<int> ans;
        while (k){
            int a = pq.top().second;
            pq.pop();
            ans.push_back(-a);
            k--;
        }
        return ans;
    }
};