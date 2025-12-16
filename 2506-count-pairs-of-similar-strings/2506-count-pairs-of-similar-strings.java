class Solution {
    public int similarPairs(String[] words) {
        Map<Integer, Integer> mp = new HashMap<>();
        int res = 0;
        
        for (String s : words) {
            int mask = 0;
            for (char c : s.toCharArray()) {
                // Set the bit corresponding to the character
                mask |= (1 << (c - 'a'));
            }
            
            // If we've seen this mask before, add the current count to result
            if (mp.containsKey(mask)) {
                res += mp.get(mask);
            }
            
            // Increment the count for this mask
            mp.put(mask, mp.getOrDefault(mask, 0) + 1);
        }
        
        return res;
    }
}