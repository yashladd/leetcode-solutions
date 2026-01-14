class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCnt = defaultdict(int)
        L = 0
        N=len(s)
        best = 0
        maxF = 0
        for R in range(N):
            charCnt[s[R]] += 1
            maxF = max(maxF, charCnt[s[R]])
            #windowSize = R - L + 1
            #mostFrequentCnt = max(charCnt.values())
            #Number of chars to change = R - L + 1 - max(charCnt.values()
            while R - L + 1 - maxF > k:
                charCnt[s[L]] -= 1
                L += 1
            best = max(best, R - L +1)
        return best