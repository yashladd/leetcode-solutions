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
        for r in range(n1):
            f1[s[r]] += 1

            if r - n2 >= 0:
                f1[s[l]] -= 1
                l += 1
            
            if f1 == f2:
                res.append(l)

        return res


