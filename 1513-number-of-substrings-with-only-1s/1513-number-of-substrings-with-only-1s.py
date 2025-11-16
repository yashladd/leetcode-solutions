class Solution:
    def numSub(self, s: str) -> int:
        i = 0
        n = len(s)
        ans = 0
        while True:
            if i >= n:
                return ans
            
            while i < n and s[i] == "0":
                i += 1
            if i < n:
                ones, l, r = 1, i, i+1
                while r < n and s[r] == "1":
                    r += 1
                    ones += 1

                subs = (ones) * (ones + 1) // 2
                ans += subs 
                ans %= 10**9 + 7
                i = r

        return (ans) % 10**9 + 7
            

