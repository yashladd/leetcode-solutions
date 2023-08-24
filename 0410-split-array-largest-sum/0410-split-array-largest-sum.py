class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canMake(s):
            cnt = 1
            currSum = 0
            for n in nums:
                if n > s:
                    return False
                if currSum + n <= s:
                    currSum += n
                else:
                    currSum = n
                    cnt += 1
                    
            return cnt <= k
                    
        lo=max(nums)
        hi=sum(nums)
        while lo <= hi:
            mid = (lo + hi) >> 1
            if canMake(mid):
                hi = mid - 1
            else: lo = mid + 1
        return lo