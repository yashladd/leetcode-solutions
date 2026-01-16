class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int l = 0;
        int r = n - 1;
        int ans = 0; // Default answer if no valid H-index is found

        while (l <= r) {
            int mid = (l + r) >>> 1;
            
            // Your requested logic:
            // Check if the paper at 'mid' has enough citations to be an H-index of (n - mid)
            if (citations[mid] >= (n - mid)) {
                ans = n - mid;  // This is a valid H-index, store it
                r = mid - 1;    // Try to find a smaller 'mid' (which yields a larger H-index)
            } else {
                l = mid + 1;    // The current H-index is too high for the citation count, move right
            }
        }
        
        return ans;
    }
}