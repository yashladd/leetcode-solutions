class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> sf = new HashMap<>(), tf = new HashMap<>();
        int n1 = s.length(), n2 = t.length();
        String res = "";
        if (n2 > n1) return res;

        for (char c: t.toCharArray()){
            tf.put(c, tf.getOrDefault(c, 0) + 1);
        }

        int required = tf.size(), l = 0, mini = Integer.MAX_VALUE;
        int matched = 0;

        for (int r = 0; r < n1; r++) {
            char c = s.charAt(r);
            sf.put(c, sf.getOrDefault(c, 0) + 1);
            if (tf.containsKey(c) && sf.get(c).intValue() == tf.get(c).intValue()) {
                matched++;
            }

            while (required == matched) {
                char leftChar = s.charAt(l);
                if (r - l + 1 < mini) {
                    mini = r - l + 1;
                    res = s.substring(l, r + 1);
                }

                sf.put(leftChar, sf.get(leftChar) - 1);
                if (tf.containsKey(leftChar) ) {
                    if (sf.get(leftChar) < tf.get(leftChar)) {
                        matched--;
                    }
                }
                l++;

            }
        }

        return res;

    }
}