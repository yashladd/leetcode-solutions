class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for p in paths:
            p = p.split(" ")

            dirr = p[0]

            for f in p[1:]:
                fName, content = f.split("(")
                content = content[:-1]
                h[content].append(dirr + "/" + fName)

        res = []
        for v in h.values():
            if len(v) > 1:
                res.append(v)

        return res

        