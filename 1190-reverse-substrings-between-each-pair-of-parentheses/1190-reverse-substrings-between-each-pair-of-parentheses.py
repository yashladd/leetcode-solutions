class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [""]

        for i, ch in enumerate(s):
            print(i, ch, stk)
            if ch == "(":
                stk.append("")
            elif ch == ")":
                last = stk.pop()
                if stk:
                    stk[-1] += last[::-1]
                else:
                    stk.append(last[::-1])
            else:
                stk[-1] += ch
        # print(stk)
        return stk[0]