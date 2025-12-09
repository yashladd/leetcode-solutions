class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def f(l, r, s):
            if len(s) == 2 * n:
                res.append(s)
                return 
            
            if l:
                f(l-1, r, s + "(")
            if r > l:
                f(l, r-1, s + ")")


        f(n, n, "")

        return res
        