class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)

        if n2 > n1:
            return []


        f1 = Counter()
        f2 = Counter(p)
        # requiredMatches = len(f2)
        # matches = 0 
        # for k, cnt in f1.items():
        #     if cnt == f2[k]:
        #         matches += 1
        """
        012345
        abcadc

        abc n2 =3
        """
        # if requiredMatches == matches:
        #     res.append(0)

        l = 0
        res = []
        requiredMatches = len(f2)
        matches = 0
        for r in range(n1):
            # 1. ADD: Update count first, THEN check for a new match
            f1[s[r]] += 1
            if s[r] in f2 and f1[s[r]] == f2[s[r]]:
                matches += 1
            
            # 2. REMOVE: If window is too big, check for broken match, THEN update count
            if r >= n2:
                if s[l] in f2 and f1[s[l]] == f2[s[l]]:
                    matches -= 1
                f1[s[l]] -= 1
                l += 1
                
            # 3. RECORD: Check matches only when window size is exactly n2
            if matches == requiredMatches:
                res.append(l)
        return res


