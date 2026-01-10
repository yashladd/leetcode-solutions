class Solution {
    public int countBattleships(char[][] board) {
    int n = board.length;
    int m = board[0].length;
    boolean[][] vis = new boolean[n][m];
    int cnt = 0;
    
    // Direction array for moving Up, Down, Left, Right
    int[][] DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // Found a new, unvisited ship part
            if (board[i][j] == 'X' && !vis[i][j]) {
                cnt++; // Increment count for this new ship
                
                // --- Start BFS to mark the rest of this ship ---
                Queue<int[]> q = new LinkedList<>();
                q.offer(new int[]{i, j});
                vis[i][j] = true;
                
                while (!q.isEmpty()) {
                    int[] curr = q.poll();
                    int r = curr[0];
                    int c = curr[1];
                    
                    for (int[] dir : DIRS) {
                        int nr = r + dir[0];
                        int nc = c + dir[1];
                        
                        // Check bounds using your helper, ensuring it's an 'X', and not visited
                        if (inb(nr, nc, n, m) && board[nr][nc] == 'X' && !vis[nr][nc]) {
                            vis[nr][nc] = true; // Mark as part of current ship
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
                // --- End BFS ---
            }
        }
    }
    return cnt;
}

// Your existing helper function
boolean inb(int nr, int nc, int n, int m) {
    return nr >= 0 && nc >= 0 && nr < n && nc < m;
}
}