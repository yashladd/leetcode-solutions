class Solution:
    def jump(self, nums: List[int]) -> int:
        j = 0
        l, r = 0, 0
        while r < len(nums)-1:
            j += 1
            maxi = l + nums[l]
            for i in range(l+1, r+1):
                maxi = max(maxi, i + nums[i])
            l = r + 1
            r = maxi
            
        return j
    
    
    
    