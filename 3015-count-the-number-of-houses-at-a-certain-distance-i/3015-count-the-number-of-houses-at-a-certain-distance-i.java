import java.util.Arrays;

class Solution {
    public int[] countOfPairs(int n, int x, int y) {
        // 1. Initialize Distance Matrix
        // Use n+1 to accommodate 1-based indexing of houses
        int[][] dist = new int[n + 1][n + 1];
        
        // Fill with a large value (infinity) initially
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dist[i], 10000); 
            dist[i][i] = 0; // Distance to self is 0
        }

        // 2. Set up initial streets (edges)
        // Linear streets: 1-2, 2-3, ...
        for (int i = 1; i < n; i++) {
            dist[i][i + 1] = 1;
            dist[i + 1][i] = 1;
        }
        
        // The shortcut street between x and y
        if (x != y) {
            dist[x][y] = 1;
            dist[y][x] = 1;
        }

        // 3. Floyd-Warshall Algorithm
        // k = intermediate node
        for (int k = 1; k <= n; k++) {
            // i = source node
            for (int i = 1; i <= n; i++) {
                // j = destination node
                for (int j = 1; j <= n; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        // 4. Count the pairs
        // result[k-1] will store the count of pairs with distance k
        int[] result = new int[n];
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i != j) {
                    int d = dist[i][j];
                    // If distance is valid, increment the corresponding index
                    if (d >= 1 && d <= n) {
                        result[d - 1]++;
                    }
                }
            }
        }
        
        return result;
    }
}