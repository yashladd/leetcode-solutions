class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        h = { ")": "(" , "}" : "{", "]" : "["}
        for ch in s:
            if ch in ["(", "{", "["]:
                stk.append(ch)
            else:
                if not stk or stk[-1] != h[ch]:
                    return False
                else:
                    stk.pop()
        return len(stk) == 0