class Solution {
    private static final int [][] DIRS = {{0,-1}, {-1,0}, {1,0}, {0,1}};

    int dfs(int i , int j , int [][]g, int n, int m, Set<String> vis) {

        int val = g[i][j];
        g[i][j] = 0;
        int maxGoldFromHere = 0;

        for (int []dir: DIRS) {
            int r = i + dir[0];
            int c = j + dir[1];
            if (r >= 0 && c >= 0 && c < m && r < n && g[r][c] != 0) {
                maxGoldFromHere = Math.max(maxGoldFromHere, dfs(r, c, g, n, m, vis));
            } 
        }
        g[i][j] = val;
        return val + maxGoldFromHere;

    }

    public int getMaximumGold(int[][] g) {

        int n = g.length, m = g[0].length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g[i][j] != 0) {
                    Set<String> vis = new HashSet<>();
                    res = Math.max(res, dfs(i, j, g, n, m, vis));
                }
            }
        }

        return res;
    }
}