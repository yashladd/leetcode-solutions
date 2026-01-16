class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> mp = new HashMap<>();

        for (int n:nums) {
            mp.put(n, mp.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(mp.get(a), mp.get(b)));

        for (Map.Entry<Integer, Integer> e: mp.entrySet()) {
            pq.add(e.getKey());
            if (pq.size() > k) pq.poll();
        }

        int[] res = new int[k];

        int idx = 0;

        while (!pq.isEmpty()) {
            res[idx++] = pq.poll();
        }

        return res;
        
    }
}