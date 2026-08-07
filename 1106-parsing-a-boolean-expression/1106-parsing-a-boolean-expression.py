class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []

        for ch in expression:
            if ch == ")":
                values = []

                while stk and stk[-1] != "(":
                    values.append(stk.pop())

                stk.pop()
                operator = stk.pop()

                res = self.evaluate(operator, values)
                stk.append(res)
            elif ch != ",":
                stk.append(ch)

        return stk[-1] == 't'


    def evaluate(self, op, values):
        if op == "!":
            return "t" if values[0] == 'f' else 'f'
        
        if op == "&":
            return 't' if all(v == 't' for v in values) else 'f'

        if op == "|":
            return 't' if any(v == 't' for v in values) else 'f'

        return 'f'
            



