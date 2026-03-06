class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res =  []
        words = set(wordDict)

        def f(i, path):
            if i == len(s):
                res.append(" ".join(path))
                return 

            
            for j in range(i+1, len(s) + 1):
                curr = s[i:j]
                if curr in words:
                    f(j, path + [curr])

        f(0, [])
        return res
