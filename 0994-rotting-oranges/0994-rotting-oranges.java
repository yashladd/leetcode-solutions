class Solution {
    public static final int[][] DIRS = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public int orangesRotting(int[][] grid) {
        // int [][] g = grid.clone();
        // Do this in interview
        Set<String> vis = new HashSet<>();

        Queue<int[]> q = new LinkedList<>();

        int n = grid.length, m = grid[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    vis.add(i + "," + j);
                    q.add(new int[]{i, j, 0});
                }
            }
        }

        int time = 0;

        while (!q.isEmpty()) {
            int [] info = q.poll();
            int r = info[0];
            int c = info[1];
            int t = info[2];

            time = Math.max(time, t);

            for (int [] dir: DIRS) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 1 && !vis.contains(nr + "," + nc))  {
                    q.add(new int [] {nr, nc, t + 1});
                    vis.add(nr + "," + nc);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    if (!vis.contains(i + "," + j)) return -1;
                }
            }
        }

        return time;
    }
}