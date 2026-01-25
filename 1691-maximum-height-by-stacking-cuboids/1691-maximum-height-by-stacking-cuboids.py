class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 1. Internal Sort: Ensure the largest dimension is the height for each cuboid.
        # This rotation strategy is optimal because height adds to value, while 
        # width/length restrict placement.
        for box in cuboids:
            box.sort()

        # 2. External Sort: Sort the list of cuboids descending (largest first).
        # This ensures that when we process cuboid 'i', all previous cuboids 'j'
        # are candidates to be the base (larger dimensions).
        cuboids.sort(reverse=True)
        
        n = len(cuboids)
        # Initialize DP with the individual height of each cuboid
        # dp[i] represents the max stack height with cuboid 'i' as the top block
        dp = [box[2] for box in cuboids]

        for i in range(1, n):
            for j in range(i):
                # Try to place cuboid 'i' (current, smaller/top) on cuboid 'j' (previous, larger/base)
                # Check all 3 dimensions: width, length, and height
                if (cuboids[j][0] >= cuboids[i][0] and 
                    cuboids[j][1] >= cuboids[i][1] and 
                    cuboids[j][2] >= cuboids[i][2]):
                    
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        
        return max(dp)