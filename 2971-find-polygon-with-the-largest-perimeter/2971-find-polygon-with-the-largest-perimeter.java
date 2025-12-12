class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long res = -1;
        long curr = 0;

        for (int n: nums) {
            if (curr > n) res = curr + n;
            curr += n;
        }

        return res;
    }
}