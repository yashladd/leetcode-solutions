import java.util.*;

class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;

        // Optimization: If k allows us to take the direct Manhattan distance path
        if (k >= m + n - 2) {
            return m + n - 2;
        }

        // State: {row, col, remaining_k}
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0, k});

        // visited[row][col] stores the maximum remaining_k seen so far at that cell
        int[][] visited = new int[m][n];
        for (int[] row : visited) {
            Arrays.fill(row, -1);
        }
        visited[0][0] = k;

        int steps = 0;
        int[][] dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        while (!q.isEmpty()) {
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                int r = curr[0];
                int c = curr[1];
                int rem = curr[2];

                // Target reached
                if (r == m - 1 && c == n - 1) {
                    return steps;
                }

                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        int newRem = rem - grid[nr][nc];

                        // Only proceed if we have removals left AND this path 
                        // provides more flexibility (higher k) than previous ones
                        if (newRem >= 0 && newRem > visited[nr][nc]) {
                            visited[nr][nc] = newRem;
                            q.offer(new int[]{nr, nc, newRem});
                        }
                    }
                }
            }
            steps++;
        }

        return -1;
    }
}