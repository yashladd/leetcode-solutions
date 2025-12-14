

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;

        // 1. Count Frequencies (Equivalent to Python's 'h = defaultdict(int)' and the first loop)
        // Key: Number, Value: Frequency
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        // 2. Create Frequency Buckets (Equivalent to Python's 'freq = [[] for _ in range(n + 1)]')
        // The array index is the frequency (0 to n). The value is a List of numbers 
        // that share that frequency.
        // We use a raw array of List<Integer> and must initialize each index.
        List<Integer>[] freqBuckets = new List[n + 1];
        for (int i = 0; i < freqBuckets.length; i++) {
            freqBuckets[i] = new ArrayList<>();
        }

        // Populate the buckets (Equivalent to Python's 'for num, f in h.items(): freq[f].append(num)')
        for (int num : counts.keySet()) {
            int freq = counts.get(num);
            freqBuckets[freq].add(num);
        }

        // 3. Collect Top K Results (Equivalent to Python's final loop)
        int[] result = new int[k];
        int resultIndex = 0;
        
        // Iterate backward from the highest possible frequency (n)
        for (int i = n; i >= 0 && resultIndex < k; i--) {
            // Check if the current bucket (frequency level) has any numbers
            for (int num : freqBuckets[i]) {
                result[resultIndex++] = num;
            }
        }
        
        return result;
    }
}