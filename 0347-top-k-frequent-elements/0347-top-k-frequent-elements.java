class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> mp = new HashMap<>();

        for (int n:nums) {
            mp.put(n, mp.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

        for (Map.Entry<Integer, Integer> e: mp.entrySet()) {
            pq.add(new int[]{e.getKey(), e.getValue()});
            if (pq.size() > k) pq.poll();
        }

        int[] res = new int[k];

        int idx = 0;

        while (!pq.isEmpty()) {
            res[idx++] = pq.poll()[0];
        }

        return res;
        
    }
}