class Solution:
    def minimumDeletions(self, s: str) -> int:
        bcnt = 0
        delete = 0 
        for i, ch in enumerate(s):
            if ch == "b":
                bcnt += 1
            else:
                delete = min(1 + delete, bcnt)
        return delete

        