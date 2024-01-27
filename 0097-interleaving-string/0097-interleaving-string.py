class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        @cache
        def f(i1, i2):
            
            if i1 == n1 and  i2 == n2:
                return True
            
            curr = i1 + i2
            
            if curr < n3 and i1 < n1 and i2 < n2:
                if s1[i1] != s3[curr] and s2[i2] != s3[curr]:
                    return False
            
            one, two = False, False
            if i1 < n1 and s1[i1] == s3[curr]:
                one = f(i1 + 1, i2)
                
            if i2 < n2 and s2[i2] == s3[curr]:
                two = f(i1, i2 + 1)
                
            return one or two
            
        return f(0, 0)