import java.util.*;

class Solution {
    public int shortestDistance(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        
        // Accumulates total distance from all buildings for each cell
        int[][] distance = new int[n][m];
        // Tracks how many buildings can reach each cell
        int[][] reach = new int[n][m];
        int totalBuildings = 0;
        
        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] == 1) {
                    totalBuildings++;
                    bfs(grid, r, c, distance, reach, directions);
                }
            }
        }
        
        int shortest = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // Check if the cell is empty land and can reach all buildings
                if (grid[i][j] == 0 && reach[i][j] == totalBuildings) {
                    shortest = Math.min(shortest, distance[i][j]);
                }
            }
        }
        
        return shortest == Integer.MAX_VALUE ? -1 : shortest;
    }
    
    private void bfs(int[][] grid, int r, int c, int[][] distance, int[][] reach, int[][] directions) {
        int n = grid.length;
        int m = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        
        q.add(new int[]{r, c, 0});
        visited[r][c] = true;
        
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int currR = curr[0];
            int currC = curr[1];
            int d = curr[2];
            
            for (int[] dir : directions) {
                int x = currR + dir[0];
                int y = currC + dir[1];
                
                // Only traverse through empty land (0)
                if (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 0 && !visited[x][y]) {
                    visited[x][y] = true;
                    distance[x][y] += d + 1;
                    reach[x][y]++;
                    q.add(new int[]{x, y, d + 1});
                }
            }
        }
    }
}