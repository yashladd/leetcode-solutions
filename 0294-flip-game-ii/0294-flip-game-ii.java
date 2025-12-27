import java.util.HashMap;
import java.util.Map;

class Solution {
    // Memoization table to store results of board states
    Map<String, Boolean> memo = new HashMap<>();

    public boolean canWin(String currentState) {
        // 1. Check if we already solved this state
        if (memo.containsKey(currentState)) {
            return memo.get(currentState);
        }

        // 2. Try every possible move
        for (int i = 0; i < currentState.length() - 1; i++) {
            // Find consecutive "++"
            if (currentState.charAt(i) == '+' && currentState.charAt(i + 1) == '+') {
                
                // Create the new state after flipping indices i and i+1
                // Note: efficient substring concatenation
                String nextState = currentState.substring(0, i) + "--" + currentState.substring(i + 2);

                // 3. If the opponent CANNOT win from this new state, then we win!
                if (!canWin(nextState)) {
                    memo.put(currentState, true);
                    return true;
                }
            }
        }

        // 4. If no move leads to a win, we lose
        memo.put(currentState, false);
        return false;
    }
}