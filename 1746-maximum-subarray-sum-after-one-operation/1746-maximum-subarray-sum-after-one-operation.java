class Solution {
    public int maxSumAfterOperation(int[] nums) {
        int currSumNoOp = 0;
        int maxi = Integer.MIN_VALUE;
        int currSumOneOp = 0;

        for (int n: nums) {
            currSumOneOp = Math.max(currSumOneOp + n, currSumNoOp + n * n);
            currSumNoOp += n;
            maxi = Math.max(maxi, currSumOneOp);
            currSumNoOp = Math.max(0, currSumNoOp);
        }
        return maxi;
    }
}