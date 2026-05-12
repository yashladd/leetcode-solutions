class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        seen = set()
        
        cnt = 0 
        
        for r, ch in enumerate(s):
            
            while len(seen) >= k or ch in seen:
                seen.discard(s[l])
                l += 1
            seen.add(ch)
            if r -l + 1 == k:
                cnt += 1
        return cnt
