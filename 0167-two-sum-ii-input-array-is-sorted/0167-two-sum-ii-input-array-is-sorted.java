class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = 0, r = nums.length-1;
        while (l < r) {
            int currSum = nums[l] + nums[r];
            if(currSum == target) {
                return new int[] {l+1, r+1};
            } else if (currSum > target) {
                r--;
            } else l++;
        }
        return new int[]{};
    }
}