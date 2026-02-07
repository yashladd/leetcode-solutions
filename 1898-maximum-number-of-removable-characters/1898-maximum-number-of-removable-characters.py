class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(k):
            
            banned = set(removable[:k])
            
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i not in banned and s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)

        l, r = 0, len(removable)
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            if isSubsequence(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return res