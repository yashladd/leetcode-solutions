class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        resLen = 0
        for i in range(n):
            #odd len
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    resLen = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                
            #even len
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    resLen = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                
        return res
        
        