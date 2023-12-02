class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def f(idx, t, res):
            if t == 0:
                ans.append(res.copy())
            for i in range(idx, len(candidates)):
                if candidates[i] > t:
                    break
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                f(i+1, t - candidates[i], res + [candidates[i]])
                
        candidates.sort()
        f(0, target, [])
        return ans
        candidates.sort()
        res = []
        n = len(candidates)
        
        def f(i, t, ds):
            if t == 0:
                res.append(ds[:])
                return 
            
            for idx in range(i, n):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue
                if candidates[i] > target: break
                f(idx+1, t-candidates[idx], ds + [candidates[idx]])
        f(0, target, [])
        return res