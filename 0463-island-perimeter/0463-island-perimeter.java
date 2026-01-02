class Solution {
    int [][] DIRS = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int dfs(int i, int j, boolean[][]vis,int  n,int m, int[][] g) {
        if (i < 0 || j < 0 || i >= n || j >= m || g[i][j] == 0) {
            return 1;
        }

        if (vis[i][j]) return 0;
        vis[i][j] = true;

        

        int per = 0;
        for (int []dir: DIRS) {
            int x = i + dir[0];
            int y = j + dir[1];
            per += dfs(x, y, vis, n, m, g);
        }

        return per;
    }
    public int islandPerimeter(int[][] g) {
        int n = g.length, m = g[0].length;
        boolean vis[][] = new boolean[n][m];
        int per = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g[i][j] == 1 && !vis[i][j])
                return dfs(i, j, vis, n, m, g);
            }
        }
        return per;
        
    }
}