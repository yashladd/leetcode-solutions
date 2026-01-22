class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        # create graph with reverse links, from child to parent
        g = defaultdict(chr)
        for l in regions:
            parent = l[0]
            for ch in l[1:]:
                g[ch] = parent
        
        p1 = region1
        p2 = region2
        while p1 != p2:
            p1 = g[p1] if p1 in g else region2
            p2 = g[p2] if p2 in g else region1
        
        return p1