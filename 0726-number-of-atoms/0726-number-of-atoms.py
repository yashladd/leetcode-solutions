class Solution:
    def countOfAtoms(self, formula: str) -> str:


        def parse_tokens(s):
            tokens = []
            N = len(s)

            i = 0
            while i < N:
                ch = s[i]
                if ch == "(":
                    tokens.append(ch)
                    i += 1
                elif ch == ")":
                    tokens.append(ch)
                    i += 1
                elif ch.isdigit():
                    num = 0

                    while i < N and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    tokens.append(num)
                elif ord('A') <= ord(ch) <= ord('Z'):
                    ele = ch
                    i += 1
                    while i < N and ord('a') <= ord(s[i]) <= ord('z'):
                        ele += s[i]
                        i += 1
                    tokens.append(ele)

            return tokens
        tokens = parse_tokens(formula)

        freq = defaultdict(int)
        """
        [(k, 4) ( (0, 1)  (N, 1)  (s, 2), (0, 6) ]
        """
        stk = []
        N = len(tokens)
        i = 0
        while i < N:
            token = tokens[i]
            if isinstance(token, int):
                if stk:
                    el, cnt = stk.pop()
                    cnt *= token
                    stk.append((el, cnt))
                i += 1
            elif token == "(":
                stk.append(token)
                i += 1
            elif token == ")":
                mult = 1
                if i + 1 < N and isinstance(tokens[i+1], int):
                    mult = tokens[i+1]
                    i += 2
                else:
                    i += 1
                values = []
                while stk and stk[-1] != "(":
                    el, cnt = stk.pop()
                    cnt *= mult
                    values.append((el, cnt))
                stk.pop()
                stk.extend(values)
            else:
                stk.append((token, 1))
                i += 1

        # print(stk)
        # print(tokens)
        for el, cnt in stk:
            freq[el] += cnt

        res = ""

        for el, cnt in sorted(freq.items(), key = lambda x: x[0]):
            res += el
            if cnt >= 2:
                res += str(cnt)

        return res

        