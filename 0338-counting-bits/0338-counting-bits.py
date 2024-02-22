class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def getCnt(n):
            cnt = 0
            while n:
                n &= n-1
                cnt += 1
            return cnt
        
        ans = []
        for i in range(n+1):
            ans.append(getCnt(i))
        return ans
            
        