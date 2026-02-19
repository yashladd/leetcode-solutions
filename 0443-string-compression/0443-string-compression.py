class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        charIdx = 0
        pos = 0

        while charIdx < n:
            currChar = chars[charIdx]
            nextCharIdx = charIdx + 1
            charCnt = 1
            while nextCharIdx < n and chars[nextCharIdx] == currChar:
                nextCharIdx += 1
                charCnt += 1
            charIdx = nextCharIdx
            chars[pos] = currChar
            pos += 1
            if charCnt == 1:
                continue
            for ch in str(int(charCnt)):
                chars[pos] = ch
                pos += 1
        
        return pos







        