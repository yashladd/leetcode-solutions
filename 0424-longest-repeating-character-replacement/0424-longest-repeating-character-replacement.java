class Solution {
    public int characterReplacement(String s, int k) {
        int freq [] = new int [26];
        int n = s.length(),l = 0, maxF = 0, res = 0;
        for (int r = 0; r < n; r++) {
            freq[Character.toUpperCase(s.charAt(r)) - 'A']++;
            maxF = Math.max(maxF, freq[Character.toUpperCase(s.charAt(r)) - 'A']);
            if (r - l + 1 - maxF > k) {
                freq[s.charAt(l++)-'A']--;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}