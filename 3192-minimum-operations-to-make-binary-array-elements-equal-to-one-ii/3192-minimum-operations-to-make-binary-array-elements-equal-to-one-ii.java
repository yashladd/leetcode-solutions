class Solution {
    public int minOperations(int[] nums) {
        int flipCnt = 0;
        for (int i = 0; i < nums.length; i++) {
            boolean isEvenFlips = flipCnt % 2 == 0;
            if((isEvenFlips && nums[i] == 0 ) || (!isEvenFlips && nums[i] == 1)) flipCnt++;
        }

        return flipCnt;
        
    }
}