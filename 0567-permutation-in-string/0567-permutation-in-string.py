class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        h1 = Counter(s1)
        for idx in range(len(s2) - len(s1)+1):
            x = s2[idx: idx + len(s1)]
            # print(x)
            if h1 == Counter(x):
                return True
            
        return False
                    
        