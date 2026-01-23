class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length;
        int [] dp = new int[n];
        Arrays.fill(dp, 1);
        Arrays.sort(nums);
        int []par = new int[n];
        for (int i = 0; i < n; i++) par[i] = i;

        int maxIdx = 0;
        int maxLen = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) {
                    if (dp[i] < 1 + dp[j]) {
                        par[i] = j;
                        dp[i] = 1 + dp[j];
                        if (dp[i] > dp[maxIdx]) maxIdx = i;
                    }
                }
            }
        }

        List<Integer> ans = new ArrayList<>();

        while (maxIdx != par[maxIdx]) {
            ans.add(nums[maxIdx]);
            maxIdx = par[maxIdx];            
        }

        ans.add(nums[maxIdx]);

        return ans;

    }
}