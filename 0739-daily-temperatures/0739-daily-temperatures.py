class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        #CONCEPT: MONOTINIC DECREASING STACK (CAN BE EQUAL)
        
        res = [0] * len(a)
        
        stk = [(a[0], 0)]
        
        for i, n in enumerate(a):
            while stk and stk[-1][0] < n:
                val, prevIdx = stk.pop()
                res[prevIdx] = i - prevIdx
            stk.append((n, i))
            
        return res
        