import java.util.*;

class Solution {
    public int countPaths(int n, int[][] roads) {
        // 1. Build the graph (Adjacency List)
        // List of {neighbor, weight} pairs
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int w = road[2];
            graph.get(u).add(new int[]{v, w});
            graph.get(v).add(new int[]{u, w});
        }

        // 2. Initialize Distances and Ways
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        long[] ways = new long[n];
        
        dist[0] = 0;
        ways[0] = 1;
        
        long MOD = 1_000_000_007;

        // 3. Priority Queue: Stores {time, node}
        // Ordered by time (ascending)
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[]{0, 0}); // {current_dist, node}

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long time = curr[0];
            int u = (int) curr[1];

            // Optimization: If we found a shorter path to u already, skip
            if (time > dist[u]) continue;

            for (int[] neighbor : graph.get(u)) {
                int v = neighbor[0];
                int w = neighbor[1];
                
                long newTime = time + w;

                // Case 1: Found a strictly shorter path
                if (newTime < dist[v]) {
                    dist[v] = newTime;
                    ways[v] = ways[u];
                    pq.offer(new long[]{newTime, v});
                } 
                // Case 2: Found another path with the same minimum time
                else if (newTime == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }

        return (int) ways[n - 1];
    }
}