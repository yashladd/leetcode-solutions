class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = defaultdict(int)
        if len(s) != len(t): return False
        for i in range(len(s)):
            h[s[i]]+=1
            h[t[i]]-=1
        # print(h, list(h.values()))
        return not any(list(h.values()))
        
        