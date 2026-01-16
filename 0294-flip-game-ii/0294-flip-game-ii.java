class Solution {
    public boolean canWin(String s) {
    // Convert to char array once at the beginning
    return canWin(s.toCharArray(), new HashMap<>());
}

    private boolean canWin(char[] arr, Map<String, Boolean> memo) {
        // 1. Must convert to String to check Memoization Key
        String key = new String(arr); 
        if (memo.containsKey(key)) return memo.get(key);

        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] == '+' && arr[i+1] == '+') {
                
                // 2. Make the Move (In-Place)
                arr[i] = '-';
                arr[i+1] = '-';
                
                // 3. Recursive Call (Pass the same array)
                // If the opponent CANNOT win, then I win.
                if (!canWin(arr, memo)) {
                    // Backtrack before returning!
                    arr[i] = '+';
                    arr[i+1] = '+';
                    
                    memo.put(key, true);
                    return true;
                }
                
                // 4. Backtrack (Undo the move for the next iteration)
                arr[i] = '+';
                arr[i+1] = '+';
            }
        }

        memo.put(key, false);
        return false;
    }
}