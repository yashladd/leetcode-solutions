class Solution {
    public int sumFourDivisors(int[] nums) {
        int maxVal = 100000; // Max constraint from problem
        int[] spf = new int[maxVal + 1]; // Smallest Prime Factor array

        // 1. Precompute SPF using Sieve
        for (int i = 0; i <= maxVal; i++) spf[i] = i;
        for (int i = 2; i * i <= maxVal; i++) {
            if (spf[i] == i) { // i is prime
                for (int j = i * i; j <= maxVal; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        int totalSum = 0;

        // 2. Process each number using SPF
        for (int num : nums) {
            // Get the first prime factor
            int p = spf[num];
            if (p == num) continue; // If num is prime, it has only 2 divisors (1, num)

            int remaining = num / p;
            
            // Case A: num = p * q (Product of two distinct primes)
            // Check if 'remaining' is a prime and distinct from 'p'
            if (spf[remaining] == remaining) {
                if (p != remaining) {
                    totalSum += (1 + p) * (1 + remaining);
                }
            } 
            // Case B: num = p^3 (Cube of a prime)
            // If remaining is not prime, check if it is p^2
            else {
                int q = spf[remaining];
                if (q == p) { // Factor must be the same prime 'p'
                    if (remaining / q == p) { // Ensure remaining was exactly p*p
                         totalSum += 1 + p + p * p + p * p * p;
                    }
                }
            }
        }

        return totalSum;
    }
}