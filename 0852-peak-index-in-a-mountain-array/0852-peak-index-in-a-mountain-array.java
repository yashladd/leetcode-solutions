class Solution {
    public int peakIndexInMountainArray(int[] a) {

        int l = 0, r = a.length - 1;

        while (l <= r) {
            int m = (l + r) >>> 1;

            if (a[m] > a[m-1] && a[m+1] < a[m]) return m;

            if (a[m] < a[m+1]) l = m;
            else r = m;

        }
        return -1;
    }
}