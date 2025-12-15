class Solution {
    boolean hasMoreChars(Map<Character, Integer> sF, Map<Character, Integer> tF) {
        for (Map.Entry<Character, Integer> e: tF.entrySet()) {
            Character c = e.getKey();
            Integer cnt = e.getValue();
            if (sF.getOrDefault(c, 0) < cnt) return true;
        }
        return false;
    }
    public String minWindow(String s, String t) {
        Map<Character, Integer> sF = new HashMap<>();
        Map<Character, Integer> tF = new HashMap<>();
        int mini = Integer.MAX_VALUE, l = 0;
        int n1 = s.length(), n2 = t.length();
        String res = "";

        if (n2 > n1) return res;

        for (char c: t.toCharArray()) {
            tF.put( c, tF.getOrDefault((c), 0) + 1);
        } 

        System.out.println(tF);

        for (int r = 0; r < n1; r++) {
            char c = s.charAt(r);
            sF.put(c, sF.getOrDefault(c, 0) + 1);

            while (!hasMoreChars(sF, tF)) {
            // 1. Update the result (since the window is currently valid)
                if (r - l + 1 < mini) {
                    mini = r - l + 1;
                    res = s.substring(l, r + 1);
                }
                
                char leftChar = s.charAt(l);
                sF.put(leftChar, sF.getOrDefault(leftChar, 0) - 1); 
                
                l++;
            }
        }

        

        return res;

    }
}