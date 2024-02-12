class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSum(s):
            subs = 1
            curr = 0
            for n in nums:
                if curr + n <= s:
                    curr += n
                else:
                    subs += 1
                    curr = n
            return subs <= k
        
        l, h = max(nums), sum(nums)
        ans = -1
        while l<= h:
            m = (l + h) >> 1
            if canSum(m):
                ans = m
                h = m-1
            else:
                l = m + 1
                
        return ans
                
                
        