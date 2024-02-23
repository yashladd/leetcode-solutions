class Solution:
    def partitionString(self, s: str) -> int:
        parts = 1
        n = len(s)
        i = 0
        flag = 0
        while i < n:
            val = ord(s[i]) - ord('a')
            if flag & (1 << val):
                parts += 1
                flag = 0
            flag |= (1 << val)
            i += 1
            
        return parts
        