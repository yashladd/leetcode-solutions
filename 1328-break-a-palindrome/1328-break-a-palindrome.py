class Solution:
    def breakPalindrome(self, pal: str) -> str:

        """
        aba
        bab -> aab

        cabac
        
        aaa

        """
        n = len(pal)
        if len(pal) == 1:
            return ""


        for i in range(len(pal)//2):
            if pal[i] != 'a':
                return pal[:i] + 'a' + pal[i+1:]


        return pal[:n-1] + 'b'
        