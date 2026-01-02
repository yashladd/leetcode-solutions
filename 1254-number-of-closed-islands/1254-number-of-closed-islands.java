class Solution {
    private static final int [][] DIRS = {{0,-1}, {-1,0}, {1,0}, {0,1}};

    boolean dfs(int i, int j, boolean[][] vis, int n, int m, int [][]g) {
        if (i < 0 || j < 0 || i >= n || j >= m) return false;
        if (g[i][j] == 1 || vis[i][j]) return true;
        vis[i][j] = true;

        // Assign each direction to a variable so they are ALL executed
boolean down  = dfs(i + 1, j, vis, n, m, g);
boolean up    = dfs(i - 1, j, vis, n, m, g);
boolean right = dfs(i, j + 1, vis, n, m, g);
boolean left  = dfs(i, j - 1, vis, n, m, g);

// Now combine the results
return down && up && right && left;

    //    return (
    //     dfs(i + 1, j, vis, n, m, g) && 
    //     dfs(i, j+1, vis, n, m, g) &&
    //     dfs(i - 1, j, vis, n, m, g) &&
    //     dfs(i, j-1, vis, n, m, g)
    //    );
    }
    public int closedIsland(int[][] g) {
        int n = g.length, m = g[0].length, res = 0;
        boolean[][]vis = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g[i][j] == 0 && !vis[i][j]) {
                    if (dfs(i, j, vis, n, m, g)) res++;
                }
            }
        }
        return res;
    }
}