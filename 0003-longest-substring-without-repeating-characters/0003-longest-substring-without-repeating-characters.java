class Solution {
    public int lengthOfLongestSubstring(String s) {

        int res = 0, n = s.length(), l = 0;

        Set<Character> m = new HashSet<>();


        for (int r = 0; r < n; r++) {
            Character c = s.charAt(r);

                while (m.contains(c)) {
                    m.remove(s.charAt(l++));
                }

                m.add(c);


            res = Math.max(res, (r-l + 1));
        }

        return res;
        
    }
}