class Solution:
    def strStr(self, s: str, p: str) -> int:
        if p == "": return 0
        """
        LPS Array Calculation for pattern: "aaacaaaa"

        Index:    0   1   2   3   4   5   6   7
        Pattern:  a   a   a   c   a   a   a   a
        LPS:      0   1   2   0   1   2   3   3

        Step-by-step trace:
        1. i=0: lps[0] is always 0.
        2. i=1: p[1]('a') == p[0]('a') -> length=1, lps[1]=1
        3. i=2: p[2]('a') == p[1]('a') -> length=2, lps[2]=2
        4. i=3: p[3]('c') != p[2]('a') -> mismatch. 
                Reduce length to lps[1]=1. p[3]('c') != p[1]('a'). 
                Reduce length to lps[0]=0. p[3]('c') != p[0]('a').
                length=0, lps[3]=0.
        5. i=4: p[4]('a') == p[0]('a') -> length=1, lps[4]=1
        6. i=5: p[5]('a') == p[1]('a') -> length=2, lps[5]=2
        7. i=6: p[6]('a') == p[2]('a') -> length=3, lps[6]=3
        8. i=7: p[7]('a') != p[3]('c') -> mismatch.
                Reduce length to lps[2]=2. p[7]('a') == p[2]('a') -> length=3, lps[7]=3.
        """

        n, m = len(s), len(p)

        lps = [0] * m

        length = 0
        i = 1

        while i < m:
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i+=1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length-1]


        i = 0
        j = 0

        while i < n:
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m 
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        
        return -1



            
            
