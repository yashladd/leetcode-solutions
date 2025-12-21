
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []

        N = len(s)

        words = set(wordDict)

        def rec(i, currWords):
            if i == N:
                if len(currWords):
                    res.append(" ".join(currWords))

            for j in range(i+1, N+1):
                currWord = s[i:j]
                if currWord in words:
                    rec(j, currWords + [currWord])
        
        rec(0, [])

        return res        