class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = [(p, s) for p, s in zip(position, speed)]
        
        stk = []
        
        for p, s in sorted(a, reverse=True):
            time = (target - p) / s
            stk.append(time)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
                
        return len(stk)