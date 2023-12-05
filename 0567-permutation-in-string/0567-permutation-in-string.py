class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        h = Counter(s1)
        matches = 0
        l1 = len(s1)
        for i in range(len(s2)):
            if s2[i] in h:
                if not h[s2[i]]: matches -=1
                h[s2[i]] -= 1
                if not h[s2[i]]: matches += 1
            if i >= l1 and s2[i-l1] in h:
                if not h[s2[i-l1]]: matches -= 1
                h[s2[i-l1]] += 1
                if not h[s2[i-l1]]: matches += 1
                
            if matches == len(h):
                return True
            
        return False
    
                    
        