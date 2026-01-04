class Solution {
    class Node {
        int r;
        int c;
        int step;
        Node(int r, int c, int step) {
            this.r = r;
            this.c = c;
            this.step = step;
        }
    }

    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        
        // "vis" array to keep track of visited cells
        boolean[][] vis = new boolean[n][m];
        
        // "dist" array to store the answer
        int[][] dist = new int[n][m];
        
        // Queue for BFS, storing {row, col, steps}
        Queue<Node> q = new LinkedList<>();
        
        // 1. Initialize the queue with all 0s
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == 0) {
                    q.add(new Node(i, j, 0)); 
                    vis[i][j] = true; 
                }
            }
        }
        
        // Direction vectors for moving up, right, down, left
        int[] dRow = {-1, 0, 1, 0};
        int[] dCol = {0, 1, 0, -1};
        
        // 2. Run standard BFS
        while (!q.isEmpty()) {
            Node curr = q.poll();
            int r = curr.r;
            int c = curr.c;
            int step = curr.step;
            
            dist[r][c] = step;
            
            for (int i = 0; i < 4; i++) {
                int nrow = r + dRow[i];
                int ncol = c + dCol[i];
                
                // Check bounds and if already visited
                if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && !vis[nrow][ncol]) {
                    vis[nrow][ncol] = true;
                    q.add(new Node(nrow, ncol, step + 1));
                }
            }
        }
        
        return dist;
    }
}