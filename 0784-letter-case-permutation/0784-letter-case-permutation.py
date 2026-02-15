class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def f(i, curr):
            if i == len(s):
                res.append("".join(curr))
                return 

            ch = s[i]
            if not ch.isalpha():
                f(i+1, curr + [ch])
            else:
                f(i+1, curr + [ch.lower()])
                f(i+1, curr + [ch.upper()])

        f(0, [])

        return res

        