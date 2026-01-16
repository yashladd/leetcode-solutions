class Solution {
    public int longestOnes(int[] nums, int k) {
        int flips = 0;
        int n = nums.length;
        int l = 0;
        int res = 0;
        for (int r = 0; r < n; r++) {
            int val = nums[r] == 1 ? 0 : 1;
            flips += val;
            while (flips > k) {
                int leftval = nums[l++] == 1 ? 0 : 1;
                flips -= leftval;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}