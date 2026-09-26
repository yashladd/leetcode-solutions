class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bc = Counter("balloon")
        tc = Counter(text)

        mini = inf

        for k, c in bc.items():
            if k not in tc or tc.get(k) < c:
                return 0
            # print(tc.get(k)//c , tc.get(k), k, c)
            mini = min(mini, tc.get(k)//c)

        return mini
