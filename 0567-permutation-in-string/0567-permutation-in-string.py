class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        h = Counter(s1)
        matches = 0
        l1 = len(s1)
        for i in range(len(s2)):
            if s2[i] in h:
                h[s2[i]] -= 1
            if i >= l1 and s2[i-l1] in h:
                h[s2[i-l1]] += 1
                
            if all([v == 0 for _, v in h.items()]):
                return True
            
        return False
    
                    
        