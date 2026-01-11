class Solution {
    public int minOperations(int[] nums) {
        /***
        Seems like need to make leftmost el 1 & progress rightwords
        [ 0  1  0  1  1  1 1 1]
        [ 1  0  1  1  1  1 1 1]
        [ 1  1  0  0  1  1 1 1]



         */

        int n = nums.length;
        int res = 0;
        for (int i = 0; i < n-2; i++) {
            if (nums[i] == 0) {
                nums[i] ^= 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                res++;
            }
        }

        if(nums[n-1] == 0 || nums[n-2] == 0) return -1;

        return res;
        
    }
}