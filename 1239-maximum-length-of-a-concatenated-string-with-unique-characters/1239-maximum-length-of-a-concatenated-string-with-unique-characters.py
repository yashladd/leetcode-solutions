class Solution:
    def maxLength(self, arr: List[str]) -> int:
        best = 0
        def f(i, res):
            nonlocal best
            if len(set(res)) != len(res):
                return 0

            if i >= len(arr):
                return len(res)

            
            best = max(best, f(i+1, res))
            best = max(best, f(i+1, res + arr[i]))
            return best

        return f(0, "")
            