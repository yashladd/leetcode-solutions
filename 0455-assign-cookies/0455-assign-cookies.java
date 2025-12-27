class Solution {
    public int findContentChildren(int[] g, int[] s) {
        /**
        []
         */

        Arrays.sort(g);
        Arrays.sort(s);

        int i = 0, j = 0;

        int res = 0;

        int n1 = g.length, n2 = s.length;

        while (i < n1 && j < n2){

            while (j < n2 && s[j] < g[i]) j++;
            if (j >= n2) return res;

            res++;
            i++;
            j++;
        }

        return res;

    }
}