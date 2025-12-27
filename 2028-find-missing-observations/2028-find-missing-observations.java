class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        /**
        sum  = ([3,2,4,3]) = 12

        m = 4, n = 2 mean = 4
        total = (4 + 2) x 4 = 24

        rem = 12

        n = 2

        [6, 6]

        21 - 12 = 9 / 4
        
        10 

        48 - 10 = 38 / 4
         */

        int sum = 0;
        for (int num: rolls) sum += num;

        int k = rolls.length + n;

        int total = k * mean;

        int missingSum = total - sum;

        // Check if valid range is possible
        if (missingSum < n || missingSum > 6 * n) {
            return new int[]{};
        }

        int part = missingSum / n;
        int remainder = missingSum % n;

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            // Start with the base value
            res[i] = part;
            // Distribute the remainder by adding 1 to the first 'remainder' elements
            if (i < remainder) {
                res[i]++;
            }
        }

        return res;
    }
}