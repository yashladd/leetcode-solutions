class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+': lambda x, y: y + x, 
              '-': lambda x, y: y - x,
              '*': lambda x, y: y * x,
              '/': lambda x, y: int(y / x)}
        s = []
        for t in tokens:
            if t in op:
                t = op[t](s.pop(), s.pop())
            s.append(int(t))
        return s[0]
        