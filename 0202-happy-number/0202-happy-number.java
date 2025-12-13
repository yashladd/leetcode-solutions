import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        seen.add(n); // Initialize set with n, matching Python logic
        int curr = n;

        while (true) {
            int newVal = getSumOfSquares(curr);
            
            if (newVal == 1) {
                return true;
            } else if (seen.contains(newVal)) {
                return false; // Cycle detected
            } else {
                seen.add(newVal);
                curr = newVal;
            }
        }
    }

    // Helper method to calculate sum of squares of digits
    // This replaces the string conversion logic: sum([int(d)**2 for d in str(curr)])
    private int getSumOfSquares(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}