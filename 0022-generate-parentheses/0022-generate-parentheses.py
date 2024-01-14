class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ds = []
        res = []
        
        def back(openCnt, closedCnt):
            if openCnt == closedCnt == n:
                res.append("".join(ds))
                return 
            
            if openCnt < n:
                ds.append("(")
                back(openCnt + 1, closedCnt)
                ds.pop()
                
            if closedCnt < openCnt:
                ds.append(")")
                back(openCnt, closedCnt + 1)
                ds.pop()
                
        back(0, 0)
        return res
        