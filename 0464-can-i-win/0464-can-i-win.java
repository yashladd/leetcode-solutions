import java.util.HashMap;
import java.util.Map;

class Solution {
    Map<Integer, Boolean> memo;
    int maxChoosableInteger;
    int desiredTotal;

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        this.maxChoosableInteger = maxChoosableInteger;
        this.desiredTotal = desiredTotal;
        int sum = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
        
        // Edge Case 1: If total sum is less than desired, no one can win
        if (sum < desiredTotal) return false;
        
        // Edge Case 2: If desiredTotal is 0, I win immediately
        if (desiredTotal <= 0) return true;

        memo = new HashMap<>();
        // 0 represents an empty set (no numbers used yet)
        return canWin(desiredTotal, 0);
    }

    private boolean canWin(int remaining, int state) {
        // Check if we already solved this state
        if (memo.containsKey(state)) return memo.get(state);

        // Try all available numbers
        for (int i = 1; i <= maxChoosableInteger; i++) {
            int currentMask = (1 << (i - 1)); // Create mask for number i
            
            // If number i is NOT used yet
            if ((state & currentMask) == 0) {
                // Win Condition:
                // 1. Picking 'i' reaches the target immediately (remaining - i <= 0)
                // 2. OR Picking 'i' forces the opponent into a losing state (!canWin)
                if (remaining - i <= 0 || !canWin(remaining - i, state | currentMask)) {
                    memo.put(state, true);
                    return true;
                }
            }
        }

        // If no move guarantees a win, then I lose
        memo.put(state, false);
        return false;
    }
}