import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> sF = new HashMap<>();
        Map<Character, Integer> tF = new HashMap<>();

        int n1 = s.length(), n2 = t.length();
        if (n2 > n1) return "";

        for (char c : t.toCharArray()) {
            tF.put(c, tF.getOrDefault(c, 0) + 1);
        }

        int required = tF.size(); // distinct chars in t that must be satisfied
        int formed = 0;           // how many are currently satisfied

        int mini = Integer.MAX_VALUE;
        int bestL = 0;
        int l = 0;
        String res = "";
        for (int r = 0; r < n1; r++) {
            char c = s.charAt(r);
            int newCount = sF.getOrDefault(c, 0) + 1;
            sF.put(c, newCount);

            // If this char is required and we just met its required count, formed++
            if (tF.containsKey(c) && newCount == tF.get(c)) {
                formed++;
            }

            // shrink only while window is valid
            while (formed == required) {
                if (r - l + 1 < mini) {
                    mini = r - l + 1;
                    bestL = l;
                    res = s.substring(l, r + 1);
                }

                char leftChar = s.charAt(l);
                int leftCount = sF.get(leftChar) - 1;
                sF.put(leftChar, leftCount);

                // If leftChar is required and we just dropped below required, formed--
                if (tF.containsKey(leftChar) && leftCount < tF.get(leftChar)) {
                    formed--;
                }

                l++;
            }
        }

        return res;
    }
}
