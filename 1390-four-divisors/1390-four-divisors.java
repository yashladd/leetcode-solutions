class Solution {
    public int sumFourDivisors(int[] nums) {
        int totalSum = 0;

        for (int num : nums) {
            int sum = 0;
            int count = 0;
            
            // We only need to loop up to the square root of num
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    // Found a divisor 'i'
                    count++;
                    sum += i;
                    
                    // If 'i' is not the square root, add the pair divisor
                    if (i * i != num) {
                        count++;
                        sum += num / i;
                    }
                }
                // Optimization: If we already exceed 4 divisors, stop early
                if (count > 4) break; 
            }

            if (count == 4) {
                totalSum += sum;
            }
        }
        
        return totalSum;
    }
}