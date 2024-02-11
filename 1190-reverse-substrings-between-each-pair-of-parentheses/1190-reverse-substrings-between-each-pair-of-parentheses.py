class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [""]
        for c in s:
            if c == "(":
                stk.append("")
            elif c == ")":
                rev = stk.pop()[::-1]
                stk[-1] += rev
            else:
                stk[-1] += c
        return "".join(stk)