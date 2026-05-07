class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not nums:
            return []
            
        # 1. Calculate prefix maximums
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], nums[i])
            
        # 2. Calculate suffix minimums
        suff_min = [0] * n
        suff_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff_min[i] = min(suff_min[i+1], nums[i])
            
        # 3. Find connected components and assign their maximums
        ans = [0] * n
        start = 0
        
        for i in range(n):
            # A component boundary is found if we are at the end, 
            # or if the max on the left is <= the min on the right
            if i == n - 1 or pref_max[i] <= suff_min[i+1]:
                
                # The maximum value in this connected chunk is simply pref_max[i]
                comp_max = pref_max[i]
                
                # Assign this maximum to every index in the current component
                for j in range(start, i + 1):
                    ans[j] = comp_max
                
                # Move the start pointer for the next component
                start = i + 1
                
        return ans