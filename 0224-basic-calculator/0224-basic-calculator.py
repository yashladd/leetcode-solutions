class Solution:
    def calculate(self, s: str) -> int:
        state = {"s": s, "it": 0}
        val, _ = self._calc(state)
        return val

    def _update(self, op, stk, val):
        if op == "+":
            stk.append(val)
        elif op == "-":
            stk.append(-val)
        elif op == "*":
            stk.append(stk.pop() * val)
        else:
            stk.append(int(stk.pop() / v))


    def _calc(self, state):
        s = state['s']
        it = state['it']
        num, stk, sign = 0, [], "+"
        while it < len(s):
            ch = s[it]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-/*":
                self._update(sign, stk, num)
                num = 0
                sign = ch
            elif ch == "(":
                state["it"] = it + 1
                num, next_it = self._calc(state)
                it = next_it
            elif ch == ")":
                self._update(sign, stk, num)
                return sum(stk), it
            it += 1

        state["it"] = it
        self._update(sign, stk, num)
        return sum(stk), it

        
