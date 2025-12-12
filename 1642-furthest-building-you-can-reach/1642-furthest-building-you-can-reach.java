class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b-a);

        int n = heights.length;

        for (int i = 1; i < n; i++) {
            if (heights[i] <= heights[i-1]) {
                continue;
            }
            int diff = heights[i] - heights[i-1];
            pq.add(diff);
            bricks -= diff;
            while (ladders > 0 && !pq.isEmpty() && bricks < 0) {
                bricks += pq.poll();
                ladders -= 1;
            } 

            if (bricks < 0) {
                return i - 1;

            }

        }


        return n-1;
    }
}