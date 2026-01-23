class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        wd = set(wordDict)

        def f(s):
            res = []
            if not s:
                return []
            if s in cache:
                return cache[s]
            for i in range(len(s)):
                word = s[:i+1]
                if word in wd:
                    # CHECK: Is this the last word in the string?
                    if i == len(s) - 1:
                        res.append(word)  # Success! Add the word alone.
                    else:
                        suffs = f(s[i+1:])
                        for suff in suffs:
                            res.append(word + " " + suff) # Add word + space + suffix

            cache[s] = res[:]
            return res

        return f(s)