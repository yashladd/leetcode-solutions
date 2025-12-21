class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        ["ac", "bb", "ca"]

        ["ca", "bb", "ac"]

        """

        N = len(strs)
        L = len(strs[0])

        prev = [""] * N
        additions = 0

        def is_sorted(curr):
            for i in range(1, N):
                if curr[i] < curr[i-1]:
                    return False
            return True


        for col in range(L):
            curr = prev[:]

            for i in range(N):
                curr[i] += strs[i][col] 

            if is_sorted(curr):
                prev = curr
                additions += 1
            
        return L - additions

        