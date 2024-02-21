class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        h = {}
        res = set()
        if len(s) <= 10:
            return []
        for i in range(len(s)-10+1):
            curr = s[i: i+10]
            if curr in h:
                res.add(curr)
            else:
                h[curr] = 1
        return list(res)

            