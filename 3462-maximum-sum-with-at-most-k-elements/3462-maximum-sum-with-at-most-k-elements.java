class Solution {
    public long maxSum(int[][] grid, int[] limits, int k) {
        List<Integer> candidates = new ArrayList<>();
        
        // Step 1: Process each row
        for (int i = 0; i < grid.length; i++) {
            // Sort the row to easily find the largest elements
            Arrays.sort(grid[i]);
            
            // Step 2: Collect the top 'limits[i]' elements from this row
            // We iterate backwards because Arrays.sort sorts in ascending order
            int count = 0;
            for (int j = grid[i].length - 1; j >= 0 && count < limits[i]; j--) {
                candidates.add(grid[i][j]);
                count++;
            }
        }
        
        // Step 3: Sort all collected candidates in descending order
        Collections.sort(candidates, Collections.reverseOrder());
        
        // Step 4: Sum the top 'k' elements
        long totalSum = 0;
        // We need to be careful not to exceed the list size if k > candidates.size()
        // (though constraints say k is valid, it's good practice)
        for (int i = 0; i < k && i < candidates.size(); i++) {
            totalSum += candidates.get(i);
        }
        
        return totalSum;
    }
}