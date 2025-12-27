class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0; // Primes must be less than n

        // 1. Create a boolean array where true means "is prime"
        // By default, boolean arrays in Java are initialized to false.
        // We use 'true' to represent primes for clarity.
        boolean[] isPrime = new boolean[n];
        for (int i = 2; i < n; i++) {
            isPrime[i] = true;
        }

        // 2. The Sieve process
        for (int p = 2; p * p < n; p++) {
            // If p is still marked as prime, mark its multiples
            if (isPrime[p]) {
                // Start marking multiples from p*p
                for (int i = p * p; i < n; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        // 3. Count remaining 'true' values
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
        }
        
        return count;
    }
}