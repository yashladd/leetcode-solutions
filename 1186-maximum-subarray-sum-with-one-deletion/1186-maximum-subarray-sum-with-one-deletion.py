class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        L = [0] * n

        L[0] = arr[0]

        for i in range(1, n):
            L[i] = max(arr[i], L[i-1] + arr[i])


        R  = [0] * n
        R[-1] = arr[-1]

        for i in range(n-2, -1, -1):
            R[i] = max(arr[i], R[i+1] + arr[i])


        best = max(L)


        for i in range(1,n-1):
            best = max(best, L[i-1] + R[i+1])

        return best