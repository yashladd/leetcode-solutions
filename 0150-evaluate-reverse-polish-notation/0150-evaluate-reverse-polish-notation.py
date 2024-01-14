class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = ["-", "+", "/", "*"]
        for t in tokens:
            # print(stk)
            if t in ops:
                op1 = stk[-2]
                op2 = stk[-1]
                stk.pop()
                stk.pop()
                val = None
                if t == "-":
                    val = op1 - op2
                elif t == "+":
                    val = op1 + op2
                elif t == "*":
                    val = op1 * op2
                else:
                    val = int(op1 / op2)
                stk.append(val)
            else:
                stk.append(int(t))
                
        return stk[0]
        