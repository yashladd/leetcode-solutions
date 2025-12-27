class Solution {
    private static final int MOD = 1_000_000_007;
    private Integer[][] memo; // Memoization table to store results

    public int numRollsToTarget(int n, int k, int target) {
        // Initialize memo table with nulls
        // Dimensions: [number of dice + 1][target sum + 1]
        memo = new Integer[n + 1][target + 1];
        return solve(n, k, target);
    }

    private int solve(int n, int k, int target) {
        // Base Case 1: If target becomes negative, this path is invalid.
        if (target < 0) return 0;
        
        // Base Case 2: If no dice are left
        if (n == 0) {
            // If target is also 0, we found a valid combination! Return 1 way.
            // Otherwise, we ran out of dice without reaching the target. Return 0.
            return target == 0 ? 1 : 0;
        }

        // Check Memoization: If we already solved this state, return the stored result.
        if (memo[n][target] != null) {
            return memo[n][target];
        }

        int ways = 0;
        
        // Iterate through all possible faces for the current die (1 to k)
        for (int face = 1; face <= k; face++) {
            // Optimization: Don't recurse if the face value is already larger than target
            if (target < face) break; 
            
            // Recursive Step: 
            // 1 die used, reduce target by 'face' value
            ways = (ways + solve(n - 1, k, target - face)) % MOD;
        }

        // Store result in memo table and return
        return memo[n][target] = ways;
    }
}