class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()

        res = []
        def f(i, curr, summ):
            """
            [10,1,2,7,6,1,5]
            [1 1 2 5 6 7 10]
            """
            if summ == target:
                res.append(curr[:])
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if summ + candidates[j] <= target:
                    f(j+1, curr + [candidates[j]], summ + candidates[j])
                else:
                    break


        f(0, [], 0)

        return res
