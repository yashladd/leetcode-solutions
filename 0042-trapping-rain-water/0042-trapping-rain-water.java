class Solution {
    public int trap(int[] g) {
        int n = g.length, l = 0, r = n-1, res = 0, 
                lMax = 0, rMax= 0;
        while (l <= r) {
            if (lMax <= rMax) {
                if (g[l] > lMax) {
                    lMax = g[l++];
                } else{
                    res += (lMax - g[l++]);
                }
            } else  {
                if (g[r] > rMax) {
                    rMax = g[r--];
                } else{
                    res += (rMax - g[r--]);
                }
            }
        }
        return res;
    }
}