class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pf = Counter(p)
        sf = Counter()
        l = 0
        res = []
        
        def check():
            for k, v in pf.items():
                if sf[k] != v:
                    return False
            return True
        
        for r, ch in enumerate(s):
            sf[ch]+=1
            
            if r >= len(p):
                sf[s[l]] -= 1
                l += 1
                
            if check():
                res.append(l)
                
        return res
                