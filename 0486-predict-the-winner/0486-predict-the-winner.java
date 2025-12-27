class Solution {
    public boolean predictTheWinner(int[] nums) {
        // If the max difference (P1 - P2) is >= 0, Player 1 wins
        return maxDiff(nums, 0, nums.length - 1) >= 0;
    }

    private int maxDiff(int[] nums, int left, int right) {
        // Base Case: If only one number is left, I take it.
        if (left == right) {
            return nums[left];
        }

        // Option 1: Pick the left number
        // My score increases by nums[left], and I subtract the best relative score 
        // the opponent can get from the rest.
        int pickLeft = nums[left] - maxDiff(nums, left + 1, right);

        // Option 2: Pick the right number
        int pickRight = nums[right] - maxDiff(nums, left, right - 1);

        // I play optimally, so I pick the option that gives me the higher difference
        return Math.max(pickLeft, pickRight);
    }
}