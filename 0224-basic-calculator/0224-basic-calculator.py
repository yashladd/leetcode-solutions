class Solution:
    operators = "+-*/"

    def calculate(self, s: str) -> int:
        state = {"s": s, "it": 0}   # mutable cursor shared across recursive calls
        value, _ = self._calc(state)
        return value

    def _update(self, op: str, v: int, stack: list) -> None:
        if op == "+":
            stack.append(v)
        elif op == "-":
            stack.append(-v)
        elif op == "*":
            stack.append(stack.pop() * v)
        elif op == "/":
            # int(a / b) truncates toward zero (python // floors, wrong for negatives)
            stack.append(int(stack.pop() / v))

    def _calc(self, state: dict):
        s = state["s"]
        num, stack, sign = 0, [], "+"
        it = state["it"]

        while it < len(s):
            ch = s[it]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in self.operators:
                self._update(sign, num, stack)
                num, sign = 0, ch
            elif ch == "(":
                state["it"] = it + 1
                num, j = self._calc(state)
                it = j
            elif ch == ")":
                self._update(sign, num, stack)
                return sum(stack), it
            # spaces fall through, no-op
            it += 1

        state["it"] = it
        self._update(sign, num, stack)   # flush the trailing operand
        return sum(stack), it