class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if len(stones) else 0
        
        S = sum(stones)
        T = S // 2
        
        @cache
        def f(i, t):
            if i == len(stones):
                return abs(T-t)
            
            pick = f(i + 1, t + stones[i])
            npick = f(i + 1, t)
            
            return min(pick, npick)
        
        diff = f(0, 0)
        posibleSum = abs(T - diff)
        remainingSum = S - posibleSum
        
        return abs(remainingSum - posibleSum)
            
        