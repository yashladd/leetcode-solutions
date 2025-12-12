class Solution {
    public record Point(int dist, int x, int y) {};
    
    public int[][] kClosest(int[][] points, int k) {
        int n = points.length; 
        
        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> b.dist - a.dist); 
        
        for (int i = 0; i < n; i++) {
            int x = points[i][0];
            int y = points[i][1];
            
            // Calculating the squared Euclidean distance: x^2 + y^2
            int dist = (int) (Math.pow(x, 2) + Math.pow(y, 2)); 
            
            if (pq.size() < k || pq.peek().dist > dist) {
                pq.add(new Point(dist, x, y));
            }

            if (pq.size() > k) {
                pq.poll();
            }
        }
        
        // Final extraction of the k closest points
        int sz = pq.size();
        int res[][] = new int[sz][2];
        
        for (int i = 0; i < sz; i++) {
            Point p = pq.poll();
            res[i][0] = p.x;
            res[i][1] = p.y;
        }
        
        return res;
    }
}