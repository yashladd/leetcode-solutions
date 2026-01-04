class Solution {
    public int getFood(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        
        // 1. Find the starting position '*'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '*') {
                    q.offer(new int[]{i, j});
                    break;
                }
            }
        }
        
        // 2. BFS Initialization
        int steps = 0;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        // 3. Process the Queue
        while (!q.isEmpty()) {
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                int r = curr[0];
                int c = curr[1];
                
                // Explore all 4 directions
                for (int[] dir : directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    
                    // Check bounds
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        // If we found food, return current steps + 1
                        if (grid[nr][nc] == '#') {
                            return steps + 1;
                        }
                        // If free space, mark as visited ('X') and add to queue
                        if (grid[nr][nc] == 'O') {
                            grid[nr][nc] = 'X'; // Mark visited
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
            }
            steps++;
        }
        
        return -1; // Food not reachable
    }
}