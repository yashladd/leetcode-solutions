class Solution {

    void swap (int [] a, int i, int j) {
        int tm = a[i];
        a[i] = a[j];
        a[j] = tm;
    }
    public void sortColors(int[] nums) {

        int l = 0, m = 0, h = nums.length-1;
        /**
         *   [2, 0, 2, 1, 1, 1]
         *    l
              m              h
             [2, 0, 2, 1, 1, 1]

            [0, 1, 2, 1, 1, 2]
             l
                m        h


         */
        while (m <= h) {
            if (nums[m] == 1){
                m++;
            } else if (nums[m] == 0) {
                swap(nums, l, m);
                l++;
                m++;
            } else {
                swap(nums, h, m);
                h--;
            }
        }
        
    }
}