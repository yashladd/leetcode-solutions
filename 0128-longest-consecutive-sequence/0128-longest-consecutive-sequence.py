class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for x in s:
            if x-1 not in s:
                l = 1
                while x + 1 in s:
                    l += 1
                    x += 1
                    
                maxi = max(maxi, l)
                
        return maxi
    
    