class Solution {
    public int lengthOfLongestSubstring(String s) {

        int res = 0, n = s.length(), l = 0;

        Map<Character, Integer> m = new HashMap<>();


        for (int r = 0; r < n; r++) {
            Character c = s.charAt(r);

            if (m.containsKey(c)) {
                l = Math.max(l, m.get(c) + 1);
            }

            m.put(c, r);


            res = Math.max(res, (r-l + 1));
        }

        return res;
        
    }
}