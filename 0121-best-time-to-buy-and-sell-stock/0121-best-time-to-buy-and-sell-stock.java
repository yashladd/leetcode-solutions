class Solution {
    public int maxProfit(int[] a) {
        int p = 0, m = a[0], n = a.length;

        for (int i = 1; i < n ; i++) {
            p = Math.max(p, a[i] - m);
            m = Math.min(m, a[i]);
        }

        return p;
    }
}