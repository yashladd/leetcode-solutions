class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tF = Counter(t)
        sF = Counter()
        i, j = 0, 0
        n = len(s)
        res = ""
        mini = float("inf")
        
        
        def check():
            for k, cnt in tF.items():
                if sF[k] < cnt:
                    return False
            return True
        
        while j < n:
            sF[s[j]] += 1
            while check():
                if j-i + 1 < mini:
                    mini = j - i + 1
                    res = s[i:j+1]
                sF[s[i]] -= 1
                i += 1
            j += 1
            
        return res
                
                