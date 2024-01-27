class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        ans = [a[0]]
        
        for i in range(1, len(a)):
            if ans[-1][1] >= a[i][0]:
                ans[-1][1] = max(ans[-1][1], a[i][1])
            else:
                ans.append(a[i])
                
        return ans
        