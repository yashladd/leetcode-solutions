class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        a b c b d a z z p
        p z z a d b c b a
        """
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        t = s[::-1]
        prev = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            curr = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return prev[n]
