class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        cnt = defaultdict(int)
        for w in words:
            for i, ch in enumerate(w):
                cnt[(i, ch)] += 1

        dp = {}
        def f(i, j):
            if j == m:
                return 1
            
            if i >= n:
                return 0


            if (i, j) in dp:
                return dp[(i, j)] 
            
            ch = target[j]

            ways = f(i+1, j)

            ways += cnt[(i, ch)] * f(i+1, j+1)
            dp[(i,j)] = ways % MOD
            return dp[(i, j)]


        return f(0, 0)