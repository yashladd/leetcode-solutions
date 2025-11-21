class Solution:
    def alienOrder(self, w: List[str]) -> str:
        g = defaultdict(list)

        distinct = set()
        indeg = defaultdict(int)

        for x in w:
            for c in x:
                distinct.add(c)
                indeg[c] = 0
        if len(distinct) == 1: return next(iter(distinct))
        prev = w[0]
        n = len(w)

        for curr in w[1:]:
            i = 0
            while i < min(len(curr), len(prev)):
                if prev[i] == curr[i]:
                    i += 1
                else:
                    break
            if i >= len(curr) and i < len(prev):
                return ""
            if i  < len(curr) and i < len(prev):
                g[prev[i]].append(curr[i])
                indeg[curr[i]] += 1
                # if prev[i] not in indeg:
                #     indeg[prev[i]] = 0
            prev = curr
            
        q = deque([])
        vis = set()
        # print(indeg, g)
        for k, v in indeg.items():
            if v == 0:
                q.append(k)
                vis.add(k)

        stk = []

        while q:
            node = q.popleft()
            stk.append(node)
            for nei in g[node]:
                indeg[nei] -= 1
                if not indeg[nei] and nei not in vis:
                    q.append(nei)
                    vis.add(nei)

        # print(distinct, stk)
        if len(stk) != len(distinct):
            return ""


        return "".join(stk)
                


        


            
        