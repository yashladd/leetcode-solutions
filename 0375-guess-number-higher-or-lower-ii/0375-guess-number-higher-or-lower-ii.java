class Solution {
    public record Range(int l, int r) {}
    int f(int l, int r, Map<Range, Integer> mp) {
        if (l >= r) return 0;
        Range thisRange = new Range(l, r);
        if (mp.containsKey(thisRange)) return mp.get(thisRange);
        
        int minCost = Integer.MAX_VALUE; // Start with infinity
        
        for (int guess = l; guess <= r; guess++) {
            // 1. Calculate the cost if we pick 'guess' and it's wrong (Worst Case for this pivot)
            int incorrectGuess = guess + Math.max(
                f(l, guess - 1, mp), 
                f(guess + 1, r, mp)
            );
            
            // 2. We want the strategy that MINIMIZES this worst-case cost
            minCost = Math.min(minCost, incorrectGuess);
        }

        mp.put(thisRange, minCost);
        
        return minCost;
    }
    public int getMoneyAmount(int n) {
        Map<Range, Integer> mp = new HashMap<>();
        return f(1, n, mp);
    }
}