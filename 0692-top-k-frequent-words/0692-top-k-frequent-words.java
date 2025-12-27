class Solution {
    // Record to store frequency and string pair
    // Note: Records use accessor methods like freq() and s()
    public record FreqStr(long freq, String s) {}

    public List<String> topKFrequent(String[] words, int k) {
        // 1. Count frequencies using a HashMap
        Map<String, Long> mp = new HashMap<>();
        for (String s : words) {
            mp.put(s, mp.getOrDefault(s, 0L) + 1);
        }

        // 2. Use a Min-Heap to keep the top k frequent words
        // Logic: 
        // - If frequencies differ, smaller frequency stays at top (to be removed).
        // - If frequencies are equal, lexicographically LARGER string stays at top (to be removed).
        PriorityQueue<FreqStr> q = new PriorityQueue<>((a, b) -> {
            if (a.freq() != b.freq()) {
                return Long.compare(a.freq(), b.freq());
            }
            return b.s().compareTo(a.s());
        });

        // 3. Add entries to the heap and maintain size k
        for (Map.Entry<String, Long> entry : mp.entrySet()) {
            q.offer(new FreqStr(entry.getValue(), entry.getKey()));
            if (q.size() > k) {
                q.poll();
            }
        }

        // 4. Build the final list (will be in reverse order from Min-Heap)
        List<String> res = new ArrayList<>();
        while (!q.isEmpty()) {
            res.add(q.poll().s());
        }
        
        // 5. Reverse the list to get highest frequency first
        Collections.reverse(res);
        return res;
    }
}