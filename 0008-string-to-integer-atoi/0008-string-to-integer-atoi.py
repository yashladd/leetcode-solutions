class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if not ls: return 0
        sign = -1 if ls[0] == '-' else 1
        res = 0
        i = 1 if ls[0] in ['-', "+"] else 0
        
        while i < len(ls) and ls[i].isdigit():
            res = 10 * res + ord(ls[i]) - ord('0')
            i += 1
            
        return max(-2**31, min(sign * res, 2**31-1))