class Solution {
    Map<String, Boolean> mp;
    boolean playFlipOptimally(String s, Map<String, Boolean> mp) {
        if (mp.containsKey(s)) return mp.get(s);

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '+' && s.charAt(i+1) == '+') {
                String nextState = s.substring(0, i) + "--" + s.substring(i+2, s.length());
                if (!playFlipOptimally(nextState, mp)) {
                    mp.put(s, true);
                    return mp.get(s);
                }

            }
        }
        mp.put(s, false);
        return false;
    }
    public boolean canWin(String currentState) {

        mp = new HashMap<>();

        return playFlipOptimally(currentState, mp);
        
    }
}