class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int n: nums) {
            if (m.containsKey(n)) return n;
            m.put(n, 1);
        }

        return -1;

        
    }
}