class Solution:
    def calculate(self, s: str) -> int:
        def calc(it):
            def apply(num, sign):
                if sign == "+": stk.append(num)
                elif sign == "-": stk.append(-num)
                elif sign == "*": stk.append(stk.pop() * num)
                else:  stk.append(int(stk.pop()/num))

            num, sign, stk = 0, '+', []
            while it < len(s):
                ch = s[it]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch in "+-*/":
                    apply(num, sign)
                    num, sign = 0, s[it]
                elif ch == "(":
                    num, j = calc(it+1)
                    it = j
                elif ch == ")":
                    apply(num, sign)
                    return sum(stk), it
                it += 1
            apply(num, sign)
            return sum(stk), it

        res, it =  calc(0)
        return res