class Solution {
    /**
 * <h3>Complexity Analysis</h3>
 * * <p><b>1. Complexity Without Memoization (Pure Backtracking)</b><br>
 * The unoptimized approach tries every possible move and recursively tries every counter-move.
 * </p>
 * <ul>
 * <li><b>Time Complexity: O(N!!) (Double Factorial)</b>
 * <ul>
 * <li>The complexity is determined by the "Game Tree" size.</li>
 * <li><b>Branching Factor:</b> ~N-1 possible moves.</li>
 * <li><b>Depth:</b> N/2 (each move consumes 2 chars).</li>
 * <li><b>Recurrence:</b> T(N) &approx; (N-1) &times; T(N-2)</li>
 * <li><b>Expansion:</b> (N-1) &times; (N-3) &times; ... &times; 1</li>
 * <li>For N=60, this is astronomically large and will TLE.</li>
 * </ul>
 * </li>
 * <li><b>Space Complexity: O(N)</b>
 * <ul>
 * <li><b>Stack:</b> Recursion goes N/2 levels deep.</li>
 * <li><b>Storage:</b> String substrings create overhead, but stack depth is the primary constraint.</li>
 * </ul>
 * </li>
 * </ul>
 * * <p><b>2. Why is it slow? (Recurring Subproblems)</b><br>
 * Without memoization, we solve the exact same board state multiple times if reached via different move orders.
 * <br>Example Input: <code>++++++</code>
 * </p>
 * <ul>
 * <li><b>Path A:</b> Flip 0,1 then 4,5 &rarr; <code>--++--</code></li>
 * <li><b>Path B:</b> Flip 4,5 then 0,1 &rarr; <code>--++--</code></li>
 * <li>The state <code>--++--</code> is calculated twice (and its entire subtree). As N grows, redundant paths explode.</li>
 * </ul>
 * * <p><b>3. Complexity With Memoization</b><br>
 * Storing results in a <code>HashMap&lt;String, Boolean&gt;</code> ensures we calculate each unique state exactly once.
 * </p>
 * <ul>
 * <li><b>New Time Complexity: O(2^N)</b>
 * <ul>
 * <li>Depends on the number of <i>unique reachable states</i> rather than move permutations.</li>
 * <li>While theoretically exponential, in practice many states are unreachable or symmetric, making it fast enough for N=60.</li>
 * </ul>
 * </li>
 * <li><b>New Space Complexity: O(2^N)</b>
 * <ul>
 * <li><b>Trade-off:</b> We trade memory for speed.</li>
 * <li>The Map stores every unique state encountered.</li>
 * </ul>
 * </li>
 * </ul>
 * * <hr>
 * <h3>Summary Comparison</h3>
 * <table border="1">
 * <tr>
 * <th>Feature</th>
 * <th>Without Memoization</th>
 * <th>With Memoization</th>
 * </tr>
 * <tr>
 * <td><b>Logic</b></td>
 * <td>Re-solves same states</td>
 * <td>Solves unique states once</td>
 * </tr>
 * <tr>
 * <td><b>Time Complexity</b></td>
 * <td>O(N!!) (Super-Exponential)</td>
 * <td>~O(2^N) (Exponential)</td>
 * </tr>
 * <tr>
 * <td><b>Space Complexity</b></td>
 * <td>O(N) (Stack)</td>
 * <td>O(2^N) (HashMap)</td>
 * </tr>
 * <tr>
 * <td><b>Viability (N=60)</b></td>
 * <td>TLE (Impossible)</td>
 * <td>Passes</td>
 * </tr>
 * </table>
 */
    Map<String, Boolean> mp = new HashMap<>();

    public boolean canWin(String currentState) {

        if (mp.containsKey(currentState)) return mp.get(currentState);
        
        for (int i = 0; i < currentState.length() - 1; i++) {
            if (currentState.charAt(i) == '+' && currentState.charAt(i+1) == '+') {
                String nextState = currentState.substring(0, i) + "--" + currentState.substring(i+2, currentState.length());
                if (!canWin(nextState)) {
                    mp.put(currentState, true);
                    return true;
                }
            }
        }
        mp.put(currentState, false);
        return false;
    }
}