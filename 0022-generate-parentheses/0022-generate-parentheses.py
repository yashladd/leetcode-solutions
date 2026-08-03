class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def f(l_c, r_c, curr_path):
            if l_c == n and r_c == n:
                res.append("".join(curr_path[:]))
                return 

            if r_c + 1 <= l_c:
                f(l_c, r_c + 1, curr_path + [")"])

            if l_c + 1 <= n:
                f(l_c + 1, r_c, curr_path + ["("])

        
        f(0, 0, [])

        return res

        