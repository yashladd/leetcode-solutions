class Solution {
    private boolean check(int []a, int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] > 0) {
                if (b[i] < a[i]) return false;
            }
        }
        return true;
    }
    public boolean checkInclusion(String s1, String s2) {
        int freq2[] = new int[26];
        int freq1[] = new int[26];
        for (char ch: s1.toCharArray()) {
            freq1[ch-'a']++;
        }
        int l = 0, n1 = s1.length(), n2 = s2.length();

        for (int r = 0; r < n2; r++) {
            freq2[s2.charAt(r)-'a']++;
            if (r - l + 1 > n1) {
                freq2[s2.charAt(l++) - 'a']--;
            }
            if (check(freq1, freq2)) {
                return true;
            }
        }

        return false;
    }
}