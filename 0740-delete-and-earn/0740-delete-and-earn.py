class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        h = Counter(nums)
        a = sorted(list(h.keys()))
        prev, secPrev = 0, 0
        for i in range(len(a)):
            currEarn = a[i] * h[a[i]]
            if i > 0 and a[i] - a[i-1] == 1:
                tmp = prev
                prev = max(currEarn + secPrev, prev)
                secPrev = tmp
            else:
                tmp = prev
                prev = currEarn + prev
                secPrev = tmp
                
        return prev
        
            
        