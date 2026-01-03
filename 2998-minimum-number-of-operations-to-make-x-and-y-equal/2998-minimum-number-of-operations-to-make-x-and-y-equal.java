class Solution {
    Map<Integer, Integer> memo = new HashMap<>();

    public int minimumOperationsToMakeEqual(int x, int y) {
        if (x <= y) {
            return y - x; // Can only increment to catch up
        }
        if (memo.containsKey(x)) {
            return memo.get(x);
        }

        // Option 1: Just decrease 1-by-1 to reach y
        int res = x - y;

        // Option 2: Go to nearest multiple of 5 (down or up), then divide
        int distTo5 = x % 5;
        res = Math.min(res, distTo5 + 1 + minimumOperationsToMakeEqual(x / 5, y));
        res = Math.min(res, (5 - distTo5) + 1 + minimumOperationsToMakeEqual(x / 5 + 1, y));

        // Option 3: Go to nearest multiple of 11 (down or up), then divide
        int distTo11 = x % 11;
        res = Math.min(res, distTo11 + 1 + minimumOperationsToMakeEqual(x / 11, y));
        res = Math.min(res, (11 - distTo11) + 1 + minimumOperationsToMakeEqual(x / 11 + 1, y));

        memo.put(x, res);
        return res;
    }
}