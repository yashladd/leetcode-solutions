class Solution:
    def countCollisions(self, d: str) -> int:

        """
        RRL -> 3
        RRLLLL
        """
        v = []
        n = len(d)
        i = 0
        while i < n:
            cnt = 1
            while i + 1 < n and d[i] == d[i+1]:
                cnt += 1
                i += 1
            v.append((d[i], cnt))
            i += 1
        res = 0
        for i, c in enumerate(v):
            if i <= len(v) - 2:
                if c[0] == "R" and v[i+1][0] == "L":
                    res += c[1] + v[i+1][1]
                elif c[0] == "R" and v[i+1][0] == "S":
                    res += c[1]
                elif c[0] == "S" and v[i+1][0] == "L":
                    res += v[i+1][1]


        return res

        print(v)
        